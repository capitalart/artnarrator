# -*- coding: utf-8 -*-
"""Artwork-related Flask routes.

This module powers the full listing workflow from initial review to
finalisation. It handles validation, moving files, regenerating image link
lists and serving gallery pages for processed and finalised artworks.

INDEX
-----
1.  Imports and Initialisation
2.  Health Checks and Status API
3.  AI Analysis & Subprocess Helpers
4.  Validation and Data Helpers
5.  Core Navigation & Upload Routes
6.  Mockup Selection Workflow Routes
7.  Artwork Analysis Trigger Routes
8.  Artwork Editing and Listing Management
9.  Static File and Image Serving Routes
10. Composite Image Preview Routes
11. Artwork Finalisation and Gallery Routes
12. Listing State Management (Lock, Unlock, Delete)
13. Asynchronous API Endpoints
14. File Processing and Utility Helpers
"""

# ===========================================================================
# 1. Imports and Initialisation
# ===========================================================================
# This section handles all necessary imports, configuration loading, and
# the initial setup of the Flask Blueprint and logging.
# ===========================================================================

from __future__ import annotations
import json, subprocess, uuid, random, logging, shutil, os, traceback, datetime, time, sys
from pathlib import Path

# --- Local Application Imports ---
from utils.logger_utils import log_action, strip_binary
from utils.sku_assigner import peek_next_sku
from utils import ai_services
from routes import sellbrite_service
import config
from helpers.listing_utils import (
    resolve_listing_paths,
    create_unanalysed_subfolder,
    cleanup_unanalysed_folders,
)
from config import (
    PROCESSED_ROOT, FINALISED_ROOT, UNANALYSED_ROOT, ARTWORK_VAULT_ROOT,
    BASE_DIR, ANALYSIS_STATUS_FILE, PROCESSED_URL_PATH, FINALISED_URL_PATH,
    LOCKED_URL_PATH, UNANALYSED_IMG_URL_PREFIX, MOCKUP_THUMB_URL_PREFIX,
    COMPOSITE_IMG_URL_PREFIX,
)
import scripts.analyze_artwork as aa

# --- Third-Party Imports ---
from helpers.image_utils import get_image_dimensions
import io
import google.generativeai as genai
from flask import (
    Blueprint, current_app, render_template, request, redirect, url_for,
    session, flash, send_from_directory, abort, Response, jsonify,
)
import re

# --- Local Route-Specific Imports ---
from . import utils
from .utils import (
    ALLOWED_COLOURS_LOWER, relative_to_base, read_generic_text, clean_terms, infer_sku_from_filename,
    sync_filename_with_sku, is_finalised_image, get_allowed_colours,
    load_json_file_safe,
)

bp = Blueprint("artwork", __name__)

# Compatibility wrapper: some upload handlers live in `routes.artwork_routes`.
# Import the canonical implementation if available and expose a thin wrapper
# named `_process_upload_file(...)` so existing callers in this module work
# and Pylance doesn't report an undefined variable.
try:
    from .artwork_routes import _process_upload_file as _ar_process_upload_file
except Exception:
    _ar_process_upload_file = None

def _process_upload_file(file_storage, folder=None):
    """Delegate to artwork_routes._process_upload_file when available.

    The original artwork implementation expects only a single `file_storage`
    argument; older call sites passed a `folder` as a second parameter. The
    wrapper accepts both forms and forwards to the canonical function.
    """
    if _ar_process_upload_file:
        return _ar_process_upload_file(file_storage)
    raise RuntimeError("Upload processing helper not available")

# ===========================================================================
# 2. Health Checks and Status API
# ===========================================================================
# These endpoints provide status information for external services like
# OpenAI and Google, and for the background artwork analysis process.
# They are used by the frontend to monitor system health.
# ===========================================================================

@bp.get("/health/openai")
def health_openai():
    """Return status of OpenAI connection."""
    logger = logging.getLogger(__name__)
    try:
        from utils.ai_services import get_openai_client
        client = get_openai_client()
        if client is None:
            raise RuntimeError("OpenAI client not configured or failed to initialise")
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
    """Return status of Google Vision connection."""
    logger = logging.getLogger(__name__)
    try:
        genai.list_models()
        return jsonify({"ok": True})
    except Exception as exc:
        logger.error("Google health check failed: %s", exc)
        error = str(exc)
        if config.DEBUG:
            error += "\n" + traceback.format_exc()
        return jsonify({"ok": False, "error": error}), 500

load_json_file_safe(ANALYSIS_STATUS_FILE)

def _write_analysis_status(step: str, percent: int, file: str | None = None, status: str | None = None, error: str | None = None) -> None:
    """Write progress info for frontend polling."""
    logger = logging.getLogger(__name__)
    payload = {"step": step, "percent": percent, "file": file, "status": status, "error": error}
    try:
        ANALYSIS_STATUS_FILE.write_text(json.dumps({k: v for k, v in payload.items() if v is not None}))
    except Exception as exc:
        logger.error("Failed writing analysis status: %s", exc)

@bp.route("/status/analyze")
def analysis_status():
    """Return JSON progress info for the current analysis job."""
    return Response(ANALYSIS_STATUS_FILE.read_text(), mimetype="application/json")

# ===========================================================================
# 3. AI Analysis & Subprocess Helpers
# ===========================================================================

def _run_ai_analysis(img_path: Path, provider: str) -> dict:
    """Run the AI analysis script and return its JSON output."""
    logger = logging.getLogger("art_analysis")
    logger.info("[DEBUG] _run_ai_analysis: img_path=%s provider=%s", img_path, provider)

    if provider == "openai":
        cmd = [sys.executable, str(config.ANALYZE_SCRIPT_PATH), str(img_path), "--json-output"]
    else:
        raise ValueError(f"Unknown provider: {provider}")

    logger.info("[DEBUG] Subprocess cmd: %s", " ".join(cmd))
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    except subprocess.TimeoutExpired as e:
        logger.error("AI analysis timed out: %s", e)
        raise RuntimeError("AI analysis timed out") from e
    except FileNotFoundError as e:
        logger.error("Analysis script not found: %s", e)
        raise RuntimeError("Analysis script not found") from e

    if result.returncode != 0:
        msg = (result.stderr or "Unknown error").strip()
        raise RuntimeError(f"AI analysis failed: {msg}")
    
    try:
        return json.loads(result.stdout.strip())
    except json.JSONDecodeError as e:
        logger.error("JSON decode error: %s", e)
        raise RuntimeError("AI analysis output could not be parsed.") from e

def _generate_composites(seo_folder: str, log_id: str) -> None:
    """Triggers the composite generation script for a specific folder."""
    cmd = [sys.executable, str(config.GENERATE_SCRIPT_PATH), "--folder", seo_folder]
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=config.BASE_DIR, timeout=600)
    composite_log = config.LOGS_DIR / "composite-generation-logs" / f"composite_gen_{log_id}.log"
    composite_log.parent.mkdir(exist_ok=True)
    composite_log.write_text(f"=== STDOUT ===\n{result.stdout}\n\n=== STDERR ===\n{result.stderr}")
    if result.returncode != 0:
        raise RuntimeError(f"Composite generation failed ({result.returncode})")

# ===========================================================================
# 4. Validation and Data Helpers
# ===========================================================================

def validate_listing_fields(data: dict, generic_text: str) -> list[str]:
    """Return a list of validation error messages for the listing."""
    errors: list[str] = []
    if not data.get("title", "").strip(): errors.append("Title cannot be blank")
    if len(data.get("title", "")) > 140: errors.append("Title exceeds 140 characters")
    if len(data.get("tags", [])) > 13: errors.append("Too many tags (max 13)")
    for t in data.get("tags", []):
        if not t or len(t) > 20: errors.append(f"Invalid tag: '{t}'")
    return errors

def get_categories_for_aspect(aspect: str) -> list[str]:
    """Return list of mockup categories available for the given aspect."""
    base = config.MOCKUPS_CATEGORISED_DIR / aspect
    return sorted([f.name for f in base.iterdir() if f.is_dir()]) if base.exists() else []

# ===========================================================================
# 5. Core Navigation & Upload Routes
# ===========================================================================

@bp.app_context_processor
def inject_latest_artwork():
    """Injects the latest analyzed artwork data into all templates."""
    return dict(latest_artwork=utils.latest_analyzed_artwork())

@bp.route("/")
def home():
    """Renders the main home page."""
    return render_template("index.html", menu=utils.get_menu())

@bp.route("/upload", methods=["GET", "POST"])
def upload_artwork():
    """Handle new artwork file uploads and run pre-QC checks."""
    if request.method == "POST":
        files = request.files.getlist("images")
        results = []
        user = session.get("username")
        
        for f in files:
            folder = create_unanalysed_subfolder(f.filename)
            try:
                res = _process_upload_file(f, folder)
            except Exception as exc:
                logging.getLogger(__name__).error("Upload failed for %s: %s", f.filename, exc)
                res = {"original": f.filename, "success": False, "error": str(exc)}
            
            log_action("upload", res.get("original", f.filename), user, res.get("error", "uploaded"), status="success" if res.get("success") else "fail")
            results.append(res)
        
        if any(r["success"] for r in results):
            flash(f"Uploaded {sum(1 for r in results if r['success'])} file(s) successfully", "success")
        for r in [r for r in results if not r["success"]]:
            flash(f"{r['original']}: {r['error']}", "danger")

        return redirect(url_for("artwork.artworks"))
        
    return render_template("upload.html", menu=utils.get_menu())

@bp.route("/artworks")
def artworks():
    """Display lists of artworks ready for analysis, processed, and finalised."""
    processed, processed_names = utils.list_processed_artworks()
    ready = utils.list_ready_to_analyze(processed_names)
    finalised = utils.list_finalised_artworks()
    return render_template("artworks.html", ready_artworks=ready, processed_artworks=processed, finalised_artworks=finalised, menu=utils.get_menu())
    
# ===========================================================================
# 6. Mockup Selection Workflow Routes
# ===========================================================================

@bp.route("/select", methods=["GET", "POST"])
def select():
    """Display the mockup selection interface."""
    if "slots" not in session or request.args.get("reset") == "1":
        utils.init_slots()
    slots = session["slots"]
    options = utils.compute_options(slots)
    zipped = list(zip(slots, options))
    return render_template("mockup_selector.html", zipped=zipped, menu=utils.get_menu())

@bp.route("/regenerate", methods=["POST"])
def regenerate():
    """Regenerate a random mockup image for a specific slot."""
    slot_idx = int(request.form["slot"])
    slots = session.get("slots", [])
    if 0 <= slot_idx < len(slots):
        cat = slots[slot_idx]["category"]
        slots[slot_idx]["image"] = utils.random_image(cat, "4x5") # Assuming 4x5 for now
        session["slots"] = slots
    return redirect(url_for("artwork.select"))

@bp.route("/swap", methods=["POST"])
def swap():
    """Swap a mockup slot to a new category."""
    slot_idx = int(request.form["slot"])
    new_cat = request.form["new_category"]
    slots = session.get("slots", [])
    if 0 <= slot_idx < len(slots):
        slots[slot_idx]["category"] = new_cat
        slots[slot_idx]["image"] = utils.random_image(new_cat, "4x5")
        session["slots"] = slots
    return redirect(url_for("artwork.select"))

# ===========================================================================
# 7. Artwork Analysis Trigger Routes
# ===========================================================================

@bp.route("/analyze/<aspect>/<filename>", methods=["POST"], endpoint="analyze_artwork")
def analyze_artwork_route(aspect, filename):
    """Run analysis on `filename` using the selected provider."""
    logger, provider = logging.getLogger(__name__), request.form.get("provider", "openai").lower()
    base_name = Path(filename).name
    _write_analysis_status("starting", 0, base_name, status="analyzing")

    src_path = next((p for p in config.UNANALYSED_ROOT.rglob(base_name) if p.is_file()), None)
    if not src_path:
        try:
            seo_folder = utils.find_seo_folder_from_filename(aspect, filename)
            src_path = PROCESSED_ROOT / seo_folder / f"{seo_folder}.jpg"
        except FileNotFoundError: pass

    if not src_path or not src_path.exists():
        flash(f"Artwork file not found: {filename}", "danger")
        return redirect(url_for("artwork.artworks"))

    try:
        analysis_result = _run_ai_analysis(src_path, provider)

        # Defensive: ensure a dict. Some error modes return a single-item
        # list containing the dict; coerce that case. Otherwise raise.
        if isinstance(analysis_result, list) and len(analysis_result) == 1 and isinstance(analysis_result[0], dict):
            analysis_result = analysis_result[0]
        if not isinstance(analysis_result, dict):
            raise RuntimeError(f"AI analysis returned unexpected type: {type(analysis_result)}")

        seo_folder = Path(analysis_result.get("processed_folder", "")).name
        
        if not seo_folder: raise RuntimeError("Analysis script did not return a valid folder name.")

        _generate_composites(seo_folder, uuid.uuid4().hex)
        
    except Exception as exc:
        flash(f"❌ Error running analysis: {exc}", "danger")
        return redirect(url_for("artwork.artworks"))

    redirect_filename = f"{seo_folder}.jpg"
    return redirect(url_for("artwork.edit_listing", aspect=aspect, filename=redirect_filename))

# ===========================================================================
# 8. Artwork Editing and Listing Management
# ===========================================================================

@bp.route("/edit-listing/<aspect>/<filename>", methods=["GET", "POST"])
def edit_listing(aspect, filename):
    """Display and update a processed or finalised artwork listing."""
    try:
        seo_folder, folder, listing_path, finalised = resolve_listing_paths(aspect, filename)
    except FileNotFoundError:
        flash(f"Artwork not found: {filename}", "danger")
        return redirect(url_for("artwork.artworks"))
    
    data = utils.load_json_file_safe(listing_path)
    is_locked_in_vault = ARTWORK_VAULT_ROOT in folder.parents

    if request.method == "POST":
        form_data = {
            "title": request.form.get("title", "").strip(),
            "description": request.form.get("description", "").strip(),
            "tags": [t.strip() for t in request.form.get("tags", "").split(',') if t.strip()],
            "materials": [m.strip() for m in request.form.get("materials", "").split(',') if m.strip()],
        }
        data.update(form_data)
        with open(listing_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        flash("Listing updated", "success")
        return redirect(url_for("artwork.edit_listing", aspect=aspect, filename=filename))

    artwork = utils.populate_artwork_data_from_json(data, seo_folder)
    mockups = utils.get_mockup_details_for_template(data.get("mockups", []), folder, seo_folder, aspect)
    
    return render_template(
        "edit_listing.html",
        artwork=artwork,
        aspect=aspect,
        filename=filename,
        seo_folder=seo_folder,
        mockups=mockups,
        finalised=finalised,
        locked=data.get("locked", False),
        is_locked_in_vault=is_locked_in_vault,
        editable=not data.get("locked", False),
        openai_analysis=data.get("openai_analysis"),
        cache_ts=int(time.time()),
    )


# NOTE: A FastAPI-style API block was previously present here (APIRouter + async
# endpoints). That block was mistakenly pasted into this Flask blueprint file and
# introduced many undefined names (router, Depends, Request, JSONResponse, etc.).
# The Flask equivalents live elsewhere in the codebase; remove the FastAPI block
# to restore import-time stability. If you want FastAPI endpoints, re-add them in
# a dedicated FastAPI routes module with proper imports.

# End of analyze_routes.py (Flask blueprint). Remaining Flask routes are above.
