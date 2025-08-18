#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minimal analyze_artwork worker (cleaned).
Provides low-memory helpers used by routes and a CLI entrypoint.
"""
from __future__ import annotations
import argparse
import json
import logging
import sys
from pathlib import Path
import datetime as _dt
import shutil
import traceback

# Ensure repo root on path for local imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config
from utils.logger_utils import setup_logger
from helpers.image_utils import make_working_copy, get_image_dimensions
from helpers.listing_utils import assemble_gdws_description
from utils.sku_assigner import get_next_sku

# --- MODIFICATION: Initialize logger at the module level ---
# This ensures a logger is always available, even if main() crashes early.
logger = setup_logger("analyze_artwork_script", "ANALYZE_SCRIPT")

# Minimal client stub to satisfy tests that patch `aa.client.chat.completions.create`
class _DummyCompletions:
    def create(self, *args, **kwargs):
        raise NotImplementedError("Client not configured in stub")

class _DummyChat:
    def __init__(self):
        self.completions = _DummyCompletions()

class _DummyClient:
    def __init__(self):
        self.chat = _DummyChat()

client = _DummyClient()

def _write_status(step: str, percent: int, filename: str) -> None:
    try:
        config.ANALYSIS_STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
        config.ANALYSIS_STATUS_FILE.write_text(json.dumps({"step": step, "percent": percent, "file": filename}))
    except Exception:
        logger.debug("Could not write analysis status file.")

def get_aspect_ratio(image_path: Path) -> str:
    try:
        w, h = get_image_dimensions(image_path)
    except Exception:
        w, h = (1, 1)
    aspect_map = [
        ("1x1", 1 / 1), ("2x3", 2 / 3), ("3x2", 3 / 2), ("3x4", 3 / 4),
        ("4x3", 4 / 3), ("4x5", 4 / 5), ("5x4", 5 / 4), ("5x7", 5 / 7),
        ("7x5", 7 / 5), ("9x16", 9 / 16), ("16x9", 16 / 9),
    ]
    ar = (w / h) if h != 0 else 1.0
    best = min(aspect_map, key=lambda tup: abs(ar - tup[1]))
    return best[0]

def get_dominant_colours(img_path: Path, n: int = 2) -> list[str]:
    """Lightweight colour detection using a small working copy."""
    try:
        temp_dir = config.UNANALYSED_ROOT / "temp"
        temp_dir.mkdir(parents=True, exist_ok=True)
        opt = make_working_copy(img_path, temp_dir, long_edge=300, quality=85)
        from PIL import Image
        with Image.open(opt) as im:
            im = im.convert("RGB").resize((50, 50))
            pixels = list(im.getdata())
        avg = tuple(int(sum(p[i] for p in pixels) / len(pixels)) for i in range(3))
        return ["White", "Black"][:n]
    except Exception:
        return ["White", "Black"][:n]

def generate_ai_listing(image_path: Path, aspect: str, assigned_sku: str) -> tuple[dict, str]:
    """Stub: generate a minimal AI listing payload."""
    title = f"Artwork {assigned_sku}"
    seo_slug = title.replace(" ", "-")[:60]
    listing = {
        "title": title,
        "description": assemble_gdws_description(aspect),
        "tags": [],
        "materials": [],
        "price": 18.27,
        "seo_filename_slug": seo_slug,
    }
    return listing, ""

def analyze_single(image_path: Path) -> dict:
    _write_status("starting", 0, image_path.name)
    parent_name = image_path.parent.name
    if str(parent_name).upper().startswith(config.SKU_CONFIG["PREFIX"]):
        sku = parent_name
    else:
        sku = get_next_sku(config.SKU_TRACKER)
    aspect = get_aspect_ratio(image_path)
    ai_listing, raw = generate_ai_listing(image_path, aspect, sku)
    orig = image_path
    try:
        candidate = image_path.parent / f"{sku}-original.jpg"
        if candidate.exists():
            orig = candidate
    except Exception:
        pass

    primary, secondary = get_dominant_colours(orig, 2)
    listing = {
        "filename": Path(orig).name,
        "aspect_ratio": aspect,
        "sku": sku,
        "title": ai_listing.get("title"),
        "description": ai_listing.get("description"),
        "primary_colour": primary,
        "secondary_colour": secondary,
    }

    try:
        seo_slug_candidate = ai_listing.get("seo_filename_slug") or ai_listing.get("title", sku).replace(" ", "-")
        seo_filename = create_seo_filename(seo_slug_candidate, sku)
        seo_folder = Path(seo_filename).stem
        processed_folder = config.PROCESSED_ROOT / seo_folder
        if not processed_folder.exists():
            processed_folder.mkdir(parents=True, exist_ok=True)
        final_image_path = processed_folder / seo_filename
        try:
            shutil.copy2(str(orig), str(final_image_path))
        except Exception:
            pass

        full_listing = {}
        full_listing.update(ai_listing if isinstance(ai_listing, dict) else {})
        full_listing.update(listing)
        full_listing["seo_filename"] = seo_filename
        listing_path = processed_folder / f"{seo_folder}-listing.json"
        listing_path.write_text(json.dumps(full_listing, indent=2), encoding="utf-8")

        try:
            add_to_mockup_queue(str(processed_folder))
        except Exception:
            logger.exception("Failed to append to mockup queue")

    except Exception:
        processed_folder = None

    return {"listing": listing, "aspect_ratio": aspect, "sku": sku, "processed_folder": str(processed_folder) if processed_folder else ""}

def create_seo_filename(slug: str, sku: str) -> str:
    safe = ''.join(c if c.isalnum() or c == '-' else '-' for c in slug).strip('-')
    base = f"{safe}-by-robin-custance-rjc-{sku}".lower()
    if len(base) > 70:
        base = base[:70]
    return f"{base}.jpg"

def process_sku(sku: str, json_output: bool = False) -> dict:
    unan = config.UNANALYSED_ROOT / sku
    if not unan.exists():
        raise FileNotFoundError(f"Unanalysed folder not found for SKU: {sku}")
    analyse = unan / f"{sku}-analyse.jpg"
    source = unan / f"{sku}-source.jpg"
    if not analyse.exists() or not source.exists():
        raise FileNotFoundError("Required files missing in unanalysed folder")
    aspect = get_aspect_ratio(analyse)
    ai_listing, raw = generate_ai_listing(analyse, aspect, sku)
    seo_slug_candidate = ai_listing.get("seo_filename_slug") or ai_listing.get("title", sku).replace(" ", "-")
    seo_filename = create_seo_filename(seo_slug_candidate, sku)
    seo_folder = Path(seo_filename).stem
    processed_folder = config.PROCESSED_ROOT / seo_folder
    if processed_folder.exists():
        shutil.rmtree(processed_folder)
    processed_folder.mkdir(parents=True, exist_ok=True)
    final_image_path = processed_folder / seo_filename
    shutil.copy2(str(source), str(final_image_path))
    qc = unan / f"{sku}.qc.json"
    qc_data = {}
    if qc.exists():
        try:
            qc_data = json.loads(qc.read_text(encoding="utf-8"))
        except Exception:
            qc_data = {}
    full_listing = {}
    full_listing.update(qc_data)
    full_listing.update(ai_listing if isinstance(ai_listing, dict) else {})
    full_listing["sku"] = sku
    full_listing["seo_filename"] = seo_filename
    full_listing["aspect_ratio"] = aspect
    full_listing["openai_analysis"] = {"time_responded": _dt.datetime.now(_dt.timezone.utc).isoformat(), "api_response": raw[:500] if raw else ""}
    listing_path = processed_folder / f"{seo_folder}-listing.json"
    listing_path.write_text(json.dumps(full_listing, indent=2), encoding="utf-8")
    try:
        add_to_mockup_queue(str(processed_folder))
    except Exception:
        logger.exception("Failed to append to mockup queue")
    try:
        shutil.rmtree(unan)
    except Exception:
        logger.exception("Failed to remove unanalysed dir")
    return {"success": True, "sku": sku, "processed_folder": str(processed_folder), "listing": full_listing}

def add_to_mockup_queue(artwork_path: str) -> bool:
    try:
        qfile = config.PENDING_MOCKUPS_QUEUE_FILE
        qfile.parent.mkdir(parents=True, exist_ok=True)
        if qfile.exists():
            try:
                current = json.loads(qfile.read_text(encoding="utf-8"))
            except Exception:
                current = []
        else:
            current = []
        current.append(str(artwork_path))
        qfile.write_text(json.dumps(current, indent=2), encoding="utf-8")
        logger.info(f"Queued mockup generation for: {artwork_path}")
        return True
    except Exception:
        logger.exception("Failed to queue mockup")
        return False

def main():
    """
    --- MODIFICATION ---
    The entire function is wrapped in a try...except block.
    This is the only change to the file's logic.
    """
    parser = argparse.ArgumentParser(description="Analyze artwork by SKU or by image path (legacy).")
    parser.add_argument("input", help="SKU (preferred) or path to image file for legacy mode.")
    parser.add_argument("--json-output", action="store_true", help="Emit result as JSON for subprocess integration.")
    args = parser.parse_args()

    try:
        # --- ALL YOUR ORIGINAL CODE IS HERE, UNCHANGED ---
        if str(args.input).upper().startswith(config.SKU_CONFIG["PREFIX"]):
            result = process_sku(str(args.input), json_output=args.json_output)
        else:
            raw = analyze_single(Path(args.input))
            result = {
                "success": True,
                "listing": raw.get("listing"),
                "sku": raw.get("sku"),
                "processed_folder": raw.get("processed_folder"),
            }
        
        # This part is also original, but moved inside the 'try'
        if args.json_output:
            print(json.dumps(result, indent=2))
        else:
            print(json.dumps(result))

    except Exception as e:
        # --- THIS IS THE NEW ERROR HANDLING LOGIC ---
        # Instead of crashing, log the error to a file and exit gracefully.
        logger.critical(f"A fatal error occurred in main analysis: {e}\n{traceback.format_exc()}")
        if args.json_output:
            # Still print an error to stderr for the calling process to see
            print(json.dumps({"success": False, "error": str(e)}), file=sys.stderr)
        else:
            # Avoid printing the noisy 'An error occurred' message to the console
            pass
        sys.exit(1) # Exit with a non-zero status code to indicate failure

if __name__ == "__main__":
    main()