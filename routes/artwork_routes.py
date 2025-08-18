# routes/artwork_routes.py
# -*- coding: utf-8 -*-
"""
Artwork-related Flask routes for the ArtNarrator application.

This module powers the entire artwork processing workflow, from initial
upload and AI analysis to mockup review, finalization, and state management.

Table of Contents (ToC)
-----------------------
[artwork-routes-py-1] Imports & Initialisation
    [artwork-routes-py-1a] Imports
    [artwork-routes-py-1b] Blueprint Setup

[artwork-routes-py-2] Health Checks and Status API
    [artwork-routes-py-2a] health_openai
    [artwork-routes-py-2b] health_google
    [artwork-routes-py-2c] _write_analysis_status
    [artwork-routes-py-2d] analysis_status

[artwork-routes-py-3] AI Analysis & Subprocess Helpers
    [artwork-routes-py-3a] _run_ai_analysis
    [artwork-routes-py-3b] _generate_composites

[artwork-routes-py-4] Validation and Data Helpers
    [artwork-routes-py-4a] validate_listing_fields
    [artwork-routes-py-4b] get_categories_for_aspect

[artwork-routes-py-5] Core Navigation & Upload Routes
    [artwork-routes-py-5a] inject_latest_artwork
    [artwork-routes-py-5b] home
    [artwork-routes-py-5c] upload_artwork
    [artwork-routes-py-5d] artworks

[artwork-routes-py-6] Mockup Selection Workflow Routes
    [artwork-routes-py-6a] select
    [artwork-routes-py-6b] regenerate
    [artwork-routes-py-6c] swap
    [artwork-routes-py-6d] proceed

[artwork-routes-py-7] Artwork Analysis Trigger Routes
    [artwork-routes-py-7a] analyze_artwork_route

[artwork-routes-py-8] Artwork Editing and Listing Management
    [artwork-routes-py-8a] edit_listing

[artwork-routes-py-9] Static File and Image Serving Routes
    [artwork-routes-py-9a] processed_image
    [artwork-routes-py-9b] finalised_image
    [artwork-routes-py-9c] locked_image
    [artwork-routes-py-9d] serve_mockup_thumb
    [artwork-routes-py-9e] unanalysed_image
    [artwork-routes-py-9f] composite_img
    [artwork-routes-py-9g] mockup_img

[artwork-routes-py-10] Composite Image Preview Routes
    [artwork-routes-py-10a] composites_preview
    [artwork-routes-py-10b] composites_specific
    [artwork-routes-py-10c] approve_composites

[artwork-routes-py-11] Artwork Finalisation and Gallery Routes
    [artwork-routes-py-11a] finalise_artwork
    [artwork-routes-py-11b] finalised_gallery
    [artwork-routes-py-11c] locked_gallery
    [artwork-routes-py-11d] lock_it_in

[artwork-routes-py-12] Listing State Management (Lock, Unlock, Delete)
    [artwork-routes-py-12a] delete_finalised
    [artwork-routes-py-12b] lock_listing
    [artwork-routes-py-12c] unlock_listing
    [artwork-routes-py-12d] unlock_artwork

[artwork-routes-py-13] Asynchronous API Endpoints
    [artwork-routes-py-13a] update_links
    [artwork-routes-py-13b] reset_sku
    [artwork-routes-py-13c] delete_artwork
    [artwork-routes-py-13d] reword_generic_text_api

[artwork-routes-py-14] File Processing and Utility Helpers
    [artwork-routes-py-14a] preview_next_sku
    [artwork-routes-py-14b] _process_upload_file

[artwork-routes-py-15] Artwork Signing Route
    [artwork-routes-py-15a] sign_artwork_route
"""

# === [ Section 1: Imports & Initialisation | artwork-routes-py-1 ] ===
from __future__ import annotations
import json, subprocess, uuid, random, logging, shutil, os, traceback, datetime, time, sys
from pathlib import Path
from PIL import Image
from helpers.image_utils import make_working_copy, get_image_dimensions
import google.generativeai as genai
from flask import (
    Blueprint, render_template, request, redirect, url_for,
    session, flash, send_from_directory, abort, Response, jsonify,
)
import re
import config
from helpers.listing_utils import (
    resolve_listing_paths,
    load_json_file_safe,
    generate_public_image_urls,
    delete_artwork as delete_artwork_files,
    update_artwork_registry,
)
import scripts.analyze_artwork as aa
from scripts import signing_service
from . import utils
from utils.logger_utils import log_action
from utils.sku_assigner import peek_next_sku, get_next_sku
from utils import ai_services
from .utils import (
    ALLOWED_COLOURS_LOWER, read_generic_text, clean_terms, infer_sku_from_filename,
    is_finalised_image, get_allowed_colours, update_listing_paths
)

# --- [ 1b: Blueprint Setup | artwork-routes-py-1b ] ---
bp = Blueprint("artwork", __name__)
logger = logging.getLogger(__name__)


# === [ Section 2: Health Checks and Status API | artwork-routes-py-2 ] ===
@bp.get("/health/openai")
def health_openai():
    """Provides a health check endpoint for the OpenAI API connection."""
    try:
        from utils.ai_services import get_openai_client
        client = get_openai_client()
        if client is None:
            raise RuntimeError("OpenAI client is not configured or failed to initialise")
        client.models.list()
        return jsonify({"ok": True})
    except Exception as exc:
        logger.error("OpenAI health check failed: %s", exc)
        error = str(exc)
        if config.DEBUG:
            error += "\n" + traceback.format_exc()
        return jsonify({"ok": False, "error": error}), 500


@bp.get("/health/google")
def health_google():
    """Provides a health check endpoint for the Google Gemini API connection."""
    try:
        genai.list_models()
        return jsonify({"ok": True})
    except Exception as exc:
        logger.error("Google health check failed: %s", exc)
        error = str(exc)
        if config.DEBUG:
            error += "\n" + traceback.format_exc()
        return jsonify({"ok": False, "error": error}), 500


def _write_analysis_status(step: str, percent: int, file: str | None = None, status: str | None = None, error: str | None = None) -> None:
    """Writes the current progress of an analysis job to a shared JSON file."""
    payload = {"step": step, "percent": percent, "file": file, "status": status, "error": error}
    try:
        config.ANALYSIS_STATUS_FILE.write_text(json.dumps({k: v for k, v in payload.items() if v is not None}))
    except Exception as exc:
        logger.error("Failed writing analysis status: %s", exc)


@bp.route("/status/analyze")
def analysis_status():
    """Returns the content of the analysis status JSON file for frontend polling."""
    try:
        text = config.ANALYSIS_STATUS_FILE.read_text()
        if not text.strip():
            return jsonify({"step": "idle", "percent": 0})
        return Response(text, mimetype="application/json")
    except Exception:
        return jsonify({"step": "idle", "percent": 0})


# === [ Section 3: AI Analysis & Subprocess Helpers | artwork-routes-py-3 ] ===
def _run_ai_analysis(img_path_or_sku, provider: str) -> dict:
    """Run the analysis CLI for either a given image path (Path) or SKU string.

    This function is tolerant for tests which call it with a Path object, and
    for production code that may pass a SKU string. It calls the CLI via
    subprocess.run and returns the parsed JSON output. Note: we intentionally
    avoid passing the `check=` kwarg so test monkeypatches that stub
    ``subprocess.run`` (without accepting `check`) remain compatible.
    """
    logger.info(f"Running AI analysis for target: {img_path_or_sku} with provider: {provider}")
    import config as _config

    # Resolve an actual filesystem path where possible
    img_path = None
    try:
        if isinstance(img_path_or_sku, Path):
            img_path = img_path_or_sku
        else:
            candidate = Path(str(img_path_or_sku))
            if candidate.exists():
                img_path = candidate
            else:
                # Treat as SKU: look for a matching file under UNANALYSED_ROOT
                search = next((p for p in _config.UNANALYSED_ROOT.rglob(str(img_path_or_sku)) if p.is_file()), None)
                if search:
                    img_path = search
    except Exception:
        img_path = None

    # Build command; if we resolved a path use it, otherwise pass the original
    target_arg = str(img_path) if img_path is not None else str(img_path_or_sku)
    cmd = [sys.executable, str(_config.ANALYZE_SCRIPT_PATH), target_arg, "--json-output"]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    except subprocess.TimeoutExpired as e:
        logger.error(f"AI analysis timed out for target {img_path_or_sku}: %s", e)
        raise RuntimeError("AI analysis timed out") from e
    except FileNotFoundError as e:
        logger.error(f"Analysis script not found for target {img_path_or_sku}: %s", e)
        raise RuntimeError("Analysis script not found") from e

    if result.returncode != 0:
        msg = (result.stderr or "Unknown error").strip()
        logger.error("AI analysis failed for %s: %s", img_path_or_sku, msg)
        raise RuntimeError(f"AI analysis failed: {msg}")

    try:
        return json.loads(result.stdout.strip())
    except json.JSONDecodeError as e:
        logger.error("Could not parse AI analysis JSON output for %s: %s", img_path_or_sku, e)
        raise RuntimeError("AI analysis output could not be parsed.") from e


def _generate_composites(log_id: str) -> None:
    """Triggers the queue-based composite/mockup generation script as a subprocess."""
    cmd = [sys.executable, str(config.GENERATE_SCRIPT_PATH)]
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=config.BASE_DIR, timeout=600)
    composite_log = config.LOGS_DIR / "composite-generation-logs" / f"composite_gen_{log_id}.log"
    composite_log.parent.mkdir(exist_ok=True, parents=True)
    composite_log.write_text(f"=== STDOUT ===\n{result.stdout}\n\n=== STDERR ===\n{result.stderr}")
    if result.returncode != 0:
        raise RuntimeError(f"Composite generation failed ({result.returncode}): {result.stderr.strip()}")


# === [ Section 4: Validation and Data Helpers | artwork-routes-py-4 ] ===
def validate_listing_fields(data: dict, generic_text: str) -> list[str]:
    """Validates all fields from the edit listing form against business rules."""
    errors: list[str] = []
    title = data.get("title", "").strip()
    if not title: errors.append("Title cannot be blank")
    if len(title) > 140: errors.append("Title exceeds 140 characters")
    tags = data.get("tags", [])
    if len(tags) > 13: errors.append("Too many tags (max 13)")
    for t in tags:
        if not t or len(t) > 20: errors.append(f"Invalid tag: '{t}'")
        if not re.fullmatch(r"[A-Za-z0-9 ]+", t): errors.append(f"Tag has invalid characters: '{t}'")
    seo_filename = data.get("seo_filename", "")
    if len(seo_filename) > 70: errors.append("SEO filename exceeds 70 characters")
    if not re.search(r"-by-robin-custance-RJC-[A-Za-z0-9-]+\.jpg$", seo_filename, re.IGNORECASE):
        errors.append("SEO filename must end with '-by-robin-custance-RJC-XXXX.jpg'")
    sku = data.get("sku", "")
    if not sku: errors.append("SKU is required")
    if sku and not sku.startswith("RJC-"): errors.append("SKU must start with 'RJC-'")
    if sku and utils.infer_sku_from_filename(seo_filename or "") != sku:
        errors.append("SKU must match value in SEO filename")
    try:
        if abs(float(data.get("price")) - 18.27) > 1e-2: errors.append("Price must be 18.27")
    except (ValueError, TypeError): errors.append("Price must be a number (18.27)")
    for key in ("primary_colour", "secondary_colour"):
        col = data.get(key, "").strip()
        if not col: errors.append(f"{key.replace('_', ' ').title()} is required")
        elif col.lower() not in utils.ALLOWED_COLOURS_LOWER: errors.append(f"{key.replace('_', ' ').title()} invalid")
    images = [i.strip() for i in data.get("images", []) if str(i).strip()]
    if not images: errors.append("At least one image required")
    desc = data.get("description", "").strip()
    if len(desc.split()) < 400: errors.append("Description must be at least 400 words")
    if generic_text and generic_text.lower() not in desc.lower():
        errors.append("Description must include the correct generic context block.")
    return errors


def get_categories_for_aspect(aspect: str) -> list[str]:
    """Returns a sorted list of available mockup category names for a given aspect ratio."""
    base = config.MOCKUPS_CATEGORISED_DIR / aspect
    return sorted([f.name for f in base.iterdir() if f.is_dir()]) if base.exists() else []


# === [ Section 5: Core Navigation & Upload Routes | artwork-routes-py-5 ] ===
@bp.app_context_processor
def inject_latest_artwork():
    """Injects data about the latest analyzed artwork into all templates."""
    return dict(latest_artwork=utils.latest_analyzed_artwork())


@bp.route("/")
def home():
    """Renders the main home/dashboard page."""
    return render_template("index.html", menu=utils.get_menu())


@bp.route("/upload", methods=["GET", "POST"])
def upload_artwork():
    """Handles new artwork file uploads and runs initial QC checks."""
    if request.method == "POST":
        files = request.files.getlist("images")
        results = []
        user = session.get("username")
        for f in files:
            try:
                res = _process_upload_file(f)
            except Exception as exc:
                logger.error("Upload failed for %s: %s", f.filename, exc, exc_info=True)
                res = {"original": f.filename, "success": False, "error": str(exc)}
            log_action("upload", res.get("original", f.filename), user, res.get("error", "uploaded"), status="success" if res.get("success") else "fail")
            results.append(res)
        
        if "XMLHttpRequest" in request.headers.get("X-Requested-With", ""):
            return jsonify(results)
        
        if any(r["success"] for r in results):
            flash(f"Uploaded {sum(1 for r in results if r['success'])} file(s) successfully. Analysis has started in the background.", "success")
        for r in [r for r in results if not r["success"]]:
            flash(f"{r['original']}: {r['error']}", "danger")

        return redirect(url_for("artwork.artworks"))
        
    return render_template("upload.html", menu=utils.get_menu())


@bp.route("/artworks")
def artworks():
    """Displays galleries of artworks in 'Ready to Analyze', 'Processed', and 'Finalised' states."""
    processed, processed_names = utils.list_processed_artworks()
    ready = utils.list_ready_to_analyze(processed_names)
    finalised = utils.list_finalised_artworks()
    return render_template("artworks.html", ready_artworks=ready, processed_artworks=processed, finalised_artworks=finalised, menu=utils.get_menu())
    

# === [ Section 6: Mockup Selection Workflow Routes (DEPRECATED) | artwork-routes-py-6 ] ===
@bp.route("/select", methods=["GET", "POST"])
def select():
    if "slots" not in session or request.args.get("reset") == "1":
        utils.init_slots()
    slots = session["slots"]
    options = utils.compute_options(slots)
    zipped = list(zip(slots, options))
    return render_template("mockup_selector.html", zipped=zipped, menu=utils.get_menu())

@bp.route("/regenerate", methods=["POST"])
def regenerate():
    slot_idx = int(request.form["slot"])
    slots = session.get("slots", [])
    if 0 <= slot_idx < len(slots):
        cat = slots[slot_idx]["category"]
        slots[slot_idx]["image"] = utils.random_image(cat, "4x5")
        session["slots"] = slots
    return redirect(url_for("artwork.select"))

@bp.route("/swap", methods=["POST"])
def swap():
    slot_idx = int(request.form["slot"])
    new_cat = request.form["new_category"]
    slots = session.get("slots", [])
    if 0 <= slot_idx < len(slots):
        slots[slot_idx]["category"] = new_cat
        slots[slot_idx]["image"] = utils.random_image(new_cat, "4x5")
        session["slots"] = slots
    return redirect(url_for("artwork.select"))

@bp.route("/proceed", methods=["POST"])
def proceed():
    flash("Composite generation process initiated!", "success")
    latest = utils.latest_composite_folder()
    if latest:
        return redirect(url_for("artwork.composites_specific", seo_folder=latest))
    return redirect(url_for("artwork.composites_preview"))


# === [ Section 7: Artwork Analysis Trigger Routes | artwork-routes-py-7 ] ===
@bp.route("/analyze/<sku>", methods=["POST"])
def analyze_artwork_route(sku: str):
    """
    Runs AI analysis on an artwork, moves it to 'processed', and renames its assets.
    This is the primary endpoint for both initial analysis and re-analysis.
    """
    provider = request.form.get("provider", "openai").lower()
    is_ajax = "XMLHttpRequest" in request.headers.get("X-Requested-With", "")

    _write_analysis_status("starting", 0, sku, status="analyzing")
    
    try:
        analysis_result = _run_ai_analysis(sku, provider)

        # Accept multiple shapes returned by the CLI or by test fakes:
        # - {'success': True, 'listing': {...}}
        # - {'listing': {...}}
        # - {'seo_filename': 'x.jpg', ...}
        if isinstance(analysis_result, list) and len(analysis_result) == 1 and isinstance(analysis_result[0], dict):
            analysis_result = analysis_result[0]

        # If the CLI returned an error wrapper
        if isinstance(analysis_result, dict) and analysis_result.get("success") is False:
            raise RuntimeError(analysis_result.get("error", "Unknown analysis error"))

        # Extract listing dict from known positions
        if isinstance(analysis_result, dict) and "listing" in analysis_result and isinstance(analysis_result["listing"], dict):
            listing = analysis_result["listing"]
        elif isinstance(analysis_result, dict) and "seo_filename" in analysis_result:
            listing = analysis_result
        else:
            listing = {}

        final_aspect = listing.get("aspect_ratio", "4x5")
        redirect_filename = listing.get("seo_filename", "") or listing.get("filename", "")

        if not redirect_filename:
            # If no filename was produced, treat as a transient failure
            raise RuntimeError("Analysis completed but did not return a valid seo_filename.")

        redirect_url = url_for("artwork.edit_listing", aspect=final_aspect, filename=redirect_filename)

        if is_ajax:
            # Strip binary-like fields before returning
            safe_listing = {k: v for k, v in listing.items() if not isinstance(v, (bytes, bytearray))}
            return jsonify({"success": True, "message": "Analysis complete.", "redirect_url": redirect_url, "listing": safe_listing})

        return redirect(redirect_url)

    except Exception as exc:
        logger.error(f"Error running analysis for SKU {sku}: {exc}", exc_info=True)
        flash(f"❌ Error running analysis: {exc}", "danger")
        if is_ajax: return jsonify({"success": False, "error": str(exc)}), 500
        return redirect(url_for("artwork.artworks"))


# Backwards-compatible filename-based analyze endpoint used by tests and older
# front-end code: accept /analyze/<aspect>/<filename> and delegate to the SKU
# based handler by locating the unanalysed file and passing its SKU/folder.
@bp.route("/analyze/<aspect>/<filename>", methods=["POST"], endpoint="analyze_artwork")
def analyze_by_filename(aspect, filename):
    # Try to find an unanalysed copy first
    import config as _config
    from pathlib import Path as _P
    base = _P(filename).name
    src = next((p for p in _config.UNANALYSED_ROOT.rglob(base) if p.is_file()), None)
    if src:
        # Run analysis directly on the image path so test fakes that expect
        # an image path are exercised and produce the mocked SEO name.
        provider = request.form.get("provider", "openai").lower()
        is_ajax = "XMLHttpRequest" in request.headers.get("X-Requested-With", "")
        try:
            analysis_result = _run_ai_analysis(src, provider)
            # Reuse the same success/listing handling as the SKU-based route
            if isinstance(analysis_result, list) and len(analysis_result) == 1 and isinstance(analysis_result[0], dict):
                analysis_result = analysis_result[0]

            if isinstance(analysis_result, dict) and analysis_result.get("success") is False:
                raise RuntimeError(analysis_result.get("error", "Unknown analysis error"))

            if isinstance(analysis_result, dict) and "listing" in analysis_result and isinstance(analysis_result["listing"], dict):
                listing = analysis_result["listing"]
            elif isinstance(analysis_result, dict) and "seo_filename" in analysis_result:
                listing = analysis_result
            else:
                listing = {}

            final_aspect = listing.get("aspect_ratio", aspect)
            redirect_filename = listing.get("seo_filename", "") or listing.get("filename", "")
            if not redirect_filename:
                raise RuntimeError("Analysis completed but did not return a valid seo_filename.")
            redirect_url = url_for("artwork.edit_listing", aspect=final_aspect, filename=redirect_filename)
            if is_ajax:
                safe_listing = {k: v for k, v in listing.items() if not isinstance(v, (bytes, bytearray))}
                return jsonify({"success": True, "redirect_url": redirect_url, "listing": safe_listing})
            return redirect(redirect_url)
        except Exception as exc:
            logger.error("Error running filename-based analysis: %s", exc, exc_info=True)
            if is_ajax:
                return jsonify({"success": False, "error": str(exc)}), 500
            flash("❌ Error running analysis.", "danger")
            return redirect(url_for("artwork.artworks"))

    # Fallback: attempt to find processed SEO folder and redirect to edit page
    try:
        seo = resolve_listing_paths(aspect, filename)[0]
        listing = load_json_file_safe(_config.PROCESSED_ROOT / seo / f"{seo}-listing.json")
        redirect_filename = listing.get("seo_filename", f"{seo}.jpg")
        return redirect(url_for("artwork.edit_listing", aspect=aspect, filename=redirect_filename))
    except Exception:
        abort(404)


# === [ Section 8: Artwork Editing and Listing Management | artwork-routes-py-8 ] ===
@bp.route("/edit-listing/<aspect>/<filename>", methods=["GET", "POST"])
def edit_listing(aspect, filename):
    try:
        seo_folder, folder, listing_path, finalised = resolve_listing_paths(aspect, filename)
    except FileNotFoundError:
        flash(f"Artwork not found: {filename}", "danger")
        return redirect(url_for("artwork.artworks"))
    
    data = load_json_file_safe(listing_path)
    is_locked_in_vault = config.ARTWORK_VAULT_ROOT in folder.parents
    stage = "vault" if is_locked_in_vault else ("finalised" if finalised else "processed")
    public_image_urls = generate_public_image_urls(seo_folder, stage)

    if request.method == "POST":
        form_data = {
            "title": request.form.get("title", "").strip(),
            "description": request.form.get("description", "").strip(),
            "tags": [t.strip() for t in request.form.get("tags", "").split(',') if t.strip()],
            "materials": [m.strip() for m in request.form.get("materials", "").split(',') if m.strip()],
            "images": [i.strip() for i in request.form.get("images", "").splitlines() if i.strip()],
        }
        data.update(form_data)
        with open(listing_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        flash("Listing updated", "success")
        return redirect(url_for("artwork.edit_listing", aspect=aspect, filename=filename))

    artwork = utils.populate_artwork_data_from_json(data, seo_folder)
    artwork["images"] = "\n".join(public_image_urls)
    mockups = utils.get_mockup_details_for_template(data.get("mockups", []), folder, seo_folder, aspect)
    
    return render_template(
        "edit_listing.html",
        artwork=artwork, aspect=aspect, filename=filename, seo_folder=seo_folder,
        mockups=mockups, finalised=finalised, locked=data.get("locked", False),
        is_locked_in_vault=is_locked_in_vault, editable=not data.get("locked", False),
        public_image_urls=public_image_urls, cache_ts=int(time.time()),
        categories=get_categories_for_aspect(aspect),
        colour_options=utils.get_allowed_colours(),
        openai_analysis=data.get("openai_analysis")
    )


# === [ Section 9: Static File and Image Serving Routes | artwork-routes-py-9 ] ===
@bp.route(f"/{config.PROCESSED_URL_PATH}/<path:filename>")
def processed_image(filename):
    return send_from_directory(config.PROCESSED_ROOT, filename)

@bp.route(f"/{config.FINALISED_URL_PATH}/<path:filename>")
def finalised_image(filename):
    return send_from_directory(config.FINALISED_ROOT, filename)

@bp.route(f"/{config.LOCKED_URL_PATH}/<path:filename>")
def locked_image(filename):
    return send_from_directory(config.ARTWORK_VAULT_ROOT, filename)

@bp.route(f"/{config.MOCKUP_THUMB_URL_PREFIX}/<path:filepath>")
def serve_mockup_thumb(filepath: str):
    for base_dir in [config.PROCESSED_ROOT, config.FINALISED_ROOT, config.ARTWORK_VAULT_ROOT]:
        full_path = base_dir / filepath
        if full_path.is_file():
            return send_from_directory(full_path.parent, full_path.name)
    abort(404)

@bp.route(f"/{config.UNANALYSED_IMG_URL_PREFIX}/<sku>/<filename>")
def unanalysed_image(sku: str, filename: str):
    path = config.UNANALYSED_ROOT / sku / filename
    if path.is_file():
        return send_from_directory(path.parent, path.name)
    abort(404)

@bp.route(f"/{config.COMPOSITE_IMG_URL_PREFIX}/<folder>/<filename>")
def composite_img(folder, filename):
    return send_from_directory(config.PROCESSED_ROOT / folder, filename)

@bp.route("/mockup-img/<category>/<filename>")
def mockup_img(category, filename):
    return send_from_directory(config.MOCKUPS_INPUT_DIR / category, filename)


# === [ Section 10: Composite Image Preview Routes | artwork-routes-py-10 ] ===
@bp.route("/composites")
def composites_preview():
    latest = utils.latest_composite_folder()
    if latest:
        return redirect(url_for("artwork.composites_specific", seo_folder=latest))
    flash("No composites found", "warning")
    return redirect(url_for("artwork.artworks"))

@bp.route("/composites/<seo_folder>")
def composites_specific(seo_folder):
    folder = config.PROCESSED_ROOT / seo_folder
    json_path = folder / f"{seo_folder}-listing.json"
    images = []
    if json_path.exists():
        listing = load_json_file_safe(json_path)
        images = utils.get_mockup_details_for_template(
            listing.get("mockups", []), folder, seo_folder, listing.get("aspect_ratio", "")
        )
    return render_template(
        "composites_preview.html", images=images, folder=seo_folder, menu=utils.get_menu()
    )

@bp.route("/approve_composites/<seo_folder>", methods=["POST"])
def approve_composites(seo_folder):
    listing_path = next((config.PROCESSED_ROOT / seo_folder).glob("*-listing.json"), None)
    if listing_path:
        data = load_json_file_safe(listing_path)
        aspect = data.get("aspect_ratio", "4x5")
        filename = data.get("seo_filename", f"{seo_folder}.jpg")
        flash("Composites approved. Please review and finalise.", "success")
        return redirect(url_for("artwork.edit_listing", aspect=aspect, filename=filename))
    flash("Could not find listing data.", "danger")
    return redirect(url_for("artwork.artworks"))


# === [ Section 11: Artwork Finalisation and Gallery Routes | artwork-routes-py-11 ] ===
@bp.post("/delete-unanalysed/<base_name>")
def delete_unanalysed(base_name: str):
    user = session.get("username", "unknown")
    try:
        if ".." in base_name or "/" in base_name:
            flash("Invalid folder name.", "danger")
            return redirect(url_for("artwork.artworks"))
        target_folder = config.UNANALYSED_ROOT / base_name
        if target_folder.is_dir():
            shutil.rmtree(target_folder)
            log_action("delete", target_folder.name, user, "Deleted unanalysed artwork folder.")
            flash(f"Artwork '{target_folder.name}' deleted successfully.", "success")
        else:
            flash(f"Could not find artwork folder for '{base_name}'.", "danger")
    except Exception as exc:
        log_action("delete", base_name, user, str(exc), status="fail")
        flash(f"An error occurred during deletion: {exc}", "danger")
    return redirect(url_for("artwork.artworks"))

@bp.route("/finalise-artwork/<seo_folder>", methods=["POST"])
def finalise_artwork(seo_folder):
    processed_path = config.PROCESSED_ROOT / seo_folder
    vault_path = config.ARTWORK_VAULT_ROOT / f"LOCKED-{seo_folder}"
    try:
        if not processed_path.exists():
            raise FileNotFoundError(f"Processed artwork '{seo_folder}' not found.")
        shutil.move(str(processed_path), str(vault_path))
        listing_file = vault_path / f"{seo_folder}-listing.json"
        utils.update_listing_paths(listing_file, config.PROCESSED_ROOT, config.ARTWORK_VAULT_ROOT)
        data = load_json_file_safe(listing_file)
        data["locked"] = True
        data["images"] = generate_public_image_urls(seo_folder, "vault")
        with open(listing_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        update_artwork_registry(seo_folder, vault_path, "locked")
        log_action("finalise", seo_folder, session.get("username"), "Artwork finalised and moved to vault")
        flash(f"Artwork '{seo_folder}' successfully finalised!", "success")
    except Exception as exc:
        flash(f"Error during finalisation: {exc}", "danger")
    return redirect(url_for("artwork.locked_gallery"))

@bp.route("/finalised")
def finalised_gallery():
    artworks = [a for a in utils.get_all_artworks() if a['status'] == 'finalised']
    return render_template("finalised.html", artworks=artworks, menu=utils.get_menu())

@bp.route("/locked")
def locked_gallery():
    locked_items = [a for a in utils.get_all_artworks() if a.get('locked')]
    return render_template("locked.html", artworks=locked_items, menu=utils.get_menu())

@bp.post("/lock-it-in/<seo_folder>")
def lock_it_in(seo_folder: str):
    processed_path = config.PROCESSED_ROOT / seo_folder
    listing_file = processed_path / f"{seo_folder}-listing.json"
    try:
        utils.assign_or_get_sku(listing_file, config.SKU_TRACKER)
        data = load_json_file_safe(listing_file)
        data["locked"] = True
        data["images"] = generate_public_image_urls(seo_folder, "processed")
        with open(listing_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        update_artwork_registry(seo_folder, processed_path, "processed")
        log_action("lock-it-in", seo_folder, session.get("username"), "Artwork locked in")
        flash("Artwork details locked. Ready for finalisation.", "success")
    except Exception as e:
        flash(f"Error locking in artwork: {e}", "danger")
    try:
        listing = load_json_file_safe(listing_file)
        aspect = listing.get("aspect_ratio", "4x5")
        filename = listing.get("seo_filename", f"{seo_folder}.jpg")
    except Exception:
        aspect = "4x5"
        filename = f"{seo_folder}.jpg"
    return redirect(url_for("artwork.edit_listing", aspect=aspect, filename=filename))


# === [ Section 12: Listing State Management (Lock, Unlock, Delete) | artwork-routes-py-12 ] ===
@bp.post("/finalise/delete/<aspect>/<filename>")
def delete_finalised(aspect, filename):
    try:
        _, folder, listing_file, _ = resolve_listing_paths(aspect, filename, allow_locked=True)
        info = load_json_file_safe(listing_file)
        if info.get("locked") and request.form.get("confirm") != "DELETE":
            flash("Type DELETE to confirm deletion of a locked item.", "warning")
            return redirect(url_for("artwork.edit_listing", aspect=aspect, filename=filename))
        shutil.rmtree(folder)
        flash("Artwork deleted successfully.", "success")
        log_action("delete", filename, session.get("username"), f"Deleted folder {folder}")
    except FileNotFoundError:
        flash("Artwork not found.", "danger")
    except Exception as e:
        flash(f"Delete failed: {e}", "danger")
    return redirect(url_for("artwork.finalised_gallery"))

@bp.post("/lock/<aspect>/<filename>")
def lock_listing(aspect, filename):
    try:
        seo, folder, listing_path, finalised = resolve_listing_paths(aspect, filename)
        if not finalised:
            flash("Artwork must be finalised before locking.", "danger")
            return redirect(url_for("artwork.edit_listing", aspect=aspect, filename=filename))
        
        target = config.ARTWORK_VAULT_ROOT / f"LOCKED-{seo}"
        config.ARTWORK_VAULT_ROOT.mkdir(parents=True, exist_ok=True)
        if target.exists(): shutil.rmtree(target)
        shutil.move(str(folder), str(target))

        new_listing_path = target / listing_path.name
        utils.update_listing_paths(new_listing_path, folder, target)
        data = load_json_file_safe(new_listing_path)
        data["locked"] = True
        data["images"] = generate_public_image_urls(seo, "vault")
        with open(new_listing_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        flash("Artwork locked.", "success")
        log_action("lock", filename, session.get("username"), "locked artwork")
    except Exception as exc:
        flash(f"Failed to lock: {exc}", "danger")
    return redirect(url_for("artwork.edit_listing", aspect=aspect, filename=filename))

@bp.post("/unlock/<aspect>/<filename>")
def unlock_listing(aspect, filename):
    if request.form.get("confirm_unlock") != "UNLOCK":
        flash("Incorrect confirmation text. Please type UNLOCK to proceed.", "warning")
        return redirect(url_for("artwork.edit_listing", aspect=aspect, filename=filename))

    try:
        _, _, listing_path, _ = resolve_listing_paths(aspect, filename, allow_locked=True)
        if config.ARTWORK_VAULT_ROOT not in listing_path.parents:
            flash("Cannot unlock an item that is not in the vault.", "danger")
            return redirect(url_for("artwork.edit_listing", aspect=aspect, filename=filename))

        with open(listing_path, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data["locked"] = False
            f.seek(0)
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.truncate()
        
        log_action("unlock", filename, session.get("username"), "unlocked artwork")
        flash("Artwork unlocked and is now editable. File paths remain unchanged.", "success")
    
    except FileNotFoundError:
        flash("Locked artwork not found.", "danger")
        return redirect(url_for("artwork.artworks"))
    except Exception as exc:
        log_action("unlock", filename, session.get("username"), "unlock failed", status="fail", error=str(exc))
        flash(f"Failed to unlock: {exc}", "danger")
        
    return redirect(url_for("artwork.edit_listing", aspect=aspect, filename=filename))

@bp.route("/unlock-artwork/<seo_folder>", methods=["POST"])
def unlock_artwork(seo_folder: str):
    locked_path = config.ARTWORK_VAULT_ROOT / f"LOCKED-{seo_folder}"
    processed_path = config.PROCESSED_ROOT / seo_folder
    try:
        shutil.move(str(locked_path), str(processed_path))
        listing_file = processed_path / f"{seo_folder}-listing.json"
        utils.update_listing_paths(listing_file, config.ARTWORK_VAULT_ROOT, config.PROCESSED_ROOT)
        data = load_json_file_safe(listing_file)
        data["locked"] = False
        data["images"] = generate_public_image_urls(seo_folder, "processed")
        with open(listing_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        update_artwork_registry(seo_folder, processed_path, "processed")
        flash("Artwork successfully unlocked.", "success")
    except Exception as exc:
        flash(f"Error during unlocking: {exc}", "danger")
    return redirect(url_for("artwork.artworks"))


# === [ Section 13: Asynchronous API Endpoints | artwork-routes-py-13 ] ===
@bp.post("/update-links/<aspect>/<filename>")
def update_links(aspect, filename):
    wants_json = "application/json" in request.headers.get("Accept", "")
    try:
        seo_folder, _, listing_file, _ = resolve_listing_paths(aspect, filename)
        stage = "vault" if (config.ARTWORK_VAULT_ROOT / f"LOCKED-{seo_folder}").exists() else "processed"
        data = load_json_file_safe(listing_file)
        data["images"] = generate_public_image_urls(seo_folder, stage)
        with open(listing_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        msg = "Image links updated"
        if wants_json: return jsonify({"success": True, "message": msg, "images": data["images"]})
        flash(msg, "success")
    except Exception as e:
        msg = f"Failed to update links: {e}"
        if wants_json: return jsonify({"success": False, "message": msg, "images": []}), 500
        flash(msg, "danger")
    return redirect(url_for("artwork.edit_listing", aspect=aspect, filename=filename))

@bp.post("/reset-sku/<aspect>/<filename>")
def reset_sku(aspect, filename):
    try:
        _, _, listing, _ = resolve_listing_paths(aspect, filename)
        utils.assign_or_get_sku(listing, config.SKU_TRACKER, force=True)
        flash("SKU has been reset.", "success")
    except Exception as exc:
        flash(f"Failed to reset SKU: {exc}", "danger")
    return redirect(url_for("artwork.edit_listing", aspect=aspect, filename=filename))

@bp.route("/delete-artwork/<sku>", methods=["POST"])
def delete_artwork(sku: str):
    user = session.get("username", "unknown")
    log_action("delete", sku, user, f"Initiating delete for '{sku}'")
    try:
        if delete_artwork_files(sku):
            flash(f"Artwork '{sku}' deleted successfully.", "success")
            log_action("delete", sku, user, "Delete process completed.")
        else:
            flash(f"Failed to delete artwork '{sku}'.", "danger")
            log_action("delete", sku, user, "Delete failed", status="fail")
    except Exception as exc:
        flash(f"An error occurred during deletion: {exc}", "danger")
        log_action("delete", sku, user, str(exc), status="fail")
    return redirect(url_for("artwork.artworks"))

@bp.post("/api/reword-generic-text")
def reword_generic_text_api():
    data = request.json
    provider = data.get("provider")
    artwork_desc = data.get("artwork_description")
    generic_text = data.get("generic_text")
    if not all([provider, artwork_desc, generic_text]):
        return jsonify({"success": False, "error": "Missing required data."}), 400
    try:
        reworded_text = ai_services.call_ai_to_reword_text(
            provider=provider,
            artwork_description=artwork_desc,
            generic_text=generic_text
        )
        return jsonify({"success": True, "reworded_text": reworded_text})
    except Exception as e:
        logger.error(f"Failed to reword generic text: {e}")
        return jsonify({"success": False, "error": str(e)}), 500


# === [ Section 14: File Processing and Utility Helpers | artwork-routes-py-14 ] ===
@bp.route("/next-sku")
def preview_next_sku():
    """Returns the next available SKU without consuming it."""
    return Response(str(peek_next_sku(config.SKU_TRACKER)), mimetype="text/plain")

def _process_upload_file(file_storage):
    """
    SKU-first upload workflow: assigns SKU, creates derivatives in 'unanalysed',
    and triggers the analysis script as a non-blocking background process.
    """
    original_filename = file_storage.filename
    if not original_filename:
        return {"original": "", "success": False, "error": "No filename provided."}
    
    ext = Path(original_filename).suffix.lower().lstrip(".")
    if ext not in config.ALLOWED_EXTENSIONS:
        return {"original": original_filename, "success": False, "error": f"Invalid file type: {ext}"}

    sku = get_next_sku(config.SKU_TRACKER)
    dest_folder = config.UNANALYSED_ROOT / sku
    dest_folder.mkdir(parents=True, exist_ok=True)

    try:
        source_path = dest_folder / f"{sku}-source.jpg"
        file_storage.save(source_path)

        # Generate derivatives
        thumb_path = dest_folder / f"{sku}-thumb.jpg"
        analyse_path = dest_folder / f"{sku}-analyse.jpg"
        
        temp_dir = dest_folder / "temp"
        temp_dir.mkdir(exist_ok=True)
        
        with Image.open(source_path) as img:
            # Create THUMB version (2000px on long edge)
            thumb_copy = make_working_copy(source_path, temp_dir, long_edge=2000, quality=90)
            shutil.move(str(thumb_copy), str(thumb_path))
            
            # Create ANALYSE version (3800px on long edge)
            analyse_copy = make_working_copy(source_path, temp_dir, long_edge=3800, quality=90)
            shutil.move(str(analyse_copy), str(analyse_path))
        
        shutil.rmtree(temp_dir) # Clean up temp sub-directory

        # Generate QC JSON
        width, height = get_image_dimensions(source_path)
        aspect = aa.get_aspect_ratio(source_path)
        qc_data = {
            "original_filename": original_filename,
            "sku": sku,
            "image_shape": [width, height],
            "filesize_bytes": source_path.stat().st_size,
            "aspect_ratio": aspect,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
        (dest_folder / f"{sku}.qc.json").write_text(json.dumps(qc_data, indent=2))

        # Trigger analysis script in the background (non-blocking)
        subprocess.Popen([sys.executable, str(config.ANALYZE_SCRIPT_PATH), sku], cwd=str(config.BASE_DIR))
        log_action("upload", sku, session.get("username", "system"), f"Queued for analysis. Files created in {dest_folder.name}")

    except Exception as exc:
        logger.error(f"Upload processing for SKU {sku} failed: {exc}", exc_info=True)
        shutil.rmtree(dest_folder, ignore_errors=True) # Cleanup on failure
        return {"original": original_filename, "success": False, "error": "Image processing failed"}

    return {"success": True, "base": sku, "original": original_filename}


# === [ Section 15: Artwork Signing Route | artwork-routes-py-15 ] ===
@bp.post("/sign-artwork/<base_name>")
def sign_artwork_route(base_name: str):
    """
    Finds an unanalysed artwork, applies a smart signature, and regenerates derivatives.
    """
    source_path = next((p for p in config.UNANALYSED_ROOT.rglob(f"{base_name}-source.jpg")), None)

    if not source_path:
        return jsonify({"success": False, "error": "Original artwork file not found."}), 404
        
    success, message = signing_service.add_smart_signature(source_path, source_path)
    
    if success:
        try:
            logger.info(f"Regenerating derivatives for signed artwork: {source_path.name}")
            dest_folder = source_path.parent
            thumb_path = dest_folder / f"{base_name}-thumb.jpg"
            analyse_path = dest_folder / f"{base_name}-analyse.jpg"
            
            temp_dir = dest_folder / "temp"
            temp_dir.mkdir(exist_ok=True)
            
            with Image.open(source_path) as img:
                thumb_copy = make_working_copy(source_path, temp_dir, long_edge=2000, quality=90)
                shutil.move(str(thumb_copy), str(thumb_path))

                analyse_copy = make_working_copy(source_path, temp_dir, long_edge=3800, quality=90)
                shutil.move(str(analyse_copy), str(analyse_path))

            logger.info(f"Successfully regenerated thumb and analyse images for {base_name}.")
            log_action("sign", source_path.name, session.get("username"), "Artwork signed and derivatives regenerated.")
            return jsonify({"success": True, "message": message})

        except Exception as e:
            error_msg = f"Artwork was signed, but failed to regenerate derivatives: {e}"
            logger.error(error_msg, exc_info=True)
            log_action("sign", source_path.name, session.get("username"), "Derivative regeneration failed.", status="fail", error=str(e))
            return jsonify({"success": True, "message": "Artwork signed, but an error occurred updating preview images."})
    else:
        log_action("sign", source_path.name, session.get("username"), "Artwork signing failed", status="fail", error=message)
        return jsonify({"success": False, "error": message}), 500
