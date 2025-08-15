#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ArtNarrator | analyze_artwork.py
===============================================================
Analyzes artworks using OpenAI. This script is the core engine that
generates listing data, processes files, and prepares artworks for the
next stage in the workflow.
"""

# ===========================================================================
# 1. Imports
# ===========================================================================
import argparse, base64, json, logging, os, re, sys, traceback
from pathlib import Path
import datetime as _dt
from dotenv import load_dotenv
from PIL import Image
from openai import OpenAI
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config
from utils.logger_utils import setup_logger
from helpers.listing_utils import assemble_gdws_description

# ===========================================================================
# 2. Configuration & Constants
# ===========================================================================
load_dotenv()
Image.MAX_IMAGE_PIXELS = None
API_KEY = config.OPENAI_API_KEY
if not API_KEY: raise RuntimeError("OPENAI_API_KEY not set in environment/.env file")
client = OpenAI(api_key=API_KEY, project=config.OPENAI_PROJECT_ID)
ETSY_COLOURS = config.ETSY_COLOURS
USER_ID = os.getenv("USER_ID", "anonymous")
logger = setup_logger(__name__, "ANALYZE_OPENAI")

# ===========================================================================
# 4. Core Utility Functions
# ===========================================================================

def _write_status(step: str, percent: int, filename: str):
    """Writes progress to the shared status file for the UI modal."""
    payload = {"step": step, "percent": percent, "file": filename, "status": "analyzing"}
    try:
        config.ANALYSIS_STATUS_FILE.write_text(json.dumps(payload), encoding="utf-8")
    except Exception:
        pass # Fails silently to not interrupt the main analysis process

def get_aspect_ratio(image_path: Path) -> str:
    """Return closest aspect ratio label for a given image."""
    with Image.open(image_path) as img: w, h = img.size
    aspect_map = [("1x1", 1/1), ("2x3", 2/3), ("3x2", 3/2), ("3x4", 3/4), ("4x3", 4/3), ("4x5", 4/5), ("5x4", 5/4), ("5x7", 5/7), ("7x5", 7/5), ("9x16", 9/16), ("16x9", 16/9)]
    ar = round(w / h, 4)
    best = min(aspect_map, key=lambda tup: abs(ar - tup[1]))
    logger.info(f"Determined aspect ratio for {image_path.name}: {best[0]}")
    return best[0]



def read_onboarding_prompt() -> str:
    """Reads the main system prompt from the file defined in config."""
    return Path(config.ONBOARDING_PATH).read_text(encoding="utf-8")


# ===========================================================================
# 5. Colour Detection & Mapping
# ===========================================================================

def _closest_colour(rgb_tuple: tuple[int, int, int]) -> str:
    min_dist = float('inf')
    best_colour = "White"
    for name, rgb in ETSY_COLOURS.items():
        dist = sum((rgb[i] - rgb_tuple[i]) ** 2 for i in range(3))
        if dist < min_dist: min_dist, best_colour = dist, name
    return best_colour

def get_dominant_colours(img_path: Path, n: int = 2) -> list[str]:
    try:
        from sklearn.cluster import KMeans
        import numpy as np
    except ImportError:
        logger.error("Scikit-learn not installed. Cannot perform color detection.")
        return ["White", "Black"]

    try:
        with Image.open(img_path) as img:
            img = img.convert("RGB").resize((100, 100))
            arr = np.asarray(img).reshape(-1, 3)
        kmeans = KMeans(n_clusters=max(3, n + 1), n_init=10, random_state=42).fit(arr)
        counts = np.bincount(kmeans.labels_)
        sorted_idx = np.argsort(counts)[::-1]
        
        colours, seen_colours = [], set()
        for i in sorted_idx:
            rgb_tuple = tuple(int(c) for c in kmeans.cluster_centers_[i])
            etsy_colour = _closest_colour(rgb_tuple)
            if etsy_colour not in seen_colours:
                seen_colours.add(etsy_colour)
                colours.append(etsy_colour)
            if len(colours) >= n: break
        
        logger.info(f"Detected dominant colours for {img_path.name}: {colours}")
        return (colours + ["White", "Black"])[:n]
    except Exception as e:
        logger.error(f"Color detection failed for {img_path.name}: {e}")
        return ["White", "Black"]

# ===========================================================================
# 6. OpenAI API Handler
# ===========================================================================

def generate_ai_listing(image_path: Path, aspect: str, assigned_sku: str) -> tuple[dict, str]:
    """Calls the OpenAI API and returns the parsed JSON and raw text."""
    logger.info(f"Preparing to call OpenAI API for {image_path.name} with SKU {assigned_sku}.")
    with open(image_path, "rb") as f:
        encoded_img = base64.b64encode(f.read()).decode("utf-8")
    
    system_prompt = Path(config.ONBOARDING_PATH).read_text(encoding="utf-8")
    
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": [{"type": "text", "text": f"Analyze this artwork (filename: {image_path.name}, aspect ratio: {aspect}) and generate the complete JSON listing. The assigned SKU is {assigned_sku}."}, {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_img}"}}]}]

    try:
        logger.info("Sending request to OpenAI ChatCompletion API...")
        response = client.chat.completions.create(model=config.OPENAI_MODEL, messages=messages, max_tokens=2100, temperature=0.92, timeout=180, response_format={"type": "json_object"})
        
        raw_text = response.choices[0].message.content
        if raw_text is None:
            logger.error("OpenAI API returned an empty response (content is None).")
            return {}, "OpenAI response was null."
            
        raw_text = raw_text.strip()
        logger.info(f"Received response from OpenAI. Raw text length: {len(raw_text)} chars.")
        return json.loads(raw_text), raw_text
        
    except json.JSONDecodeError:
        logger.warning("OpenAI response was not valid JSON. Attempting fallback parsing.")
        return parse_text_fallback(raw_text), raw_text
    except Exception as e:
        logger.error(f"OpenAI API call failed: {e}", exc_info=True)
        raise

def parse_text_fallback(text: str) -> dict:
    """Extracts listing data from non-JSON text as a last resort."""
    data = {"fallback_text": text}
    title_match = re.search(r"\"title\":\s*\"(.*?)\"", text, re.IGNORECASE)
    if title_match: data["title"] = title_match.group(1)
    return data

# ===========================================================================
# 7. Main Analysis Workflow
# ===========================================================================

def analyze_single(image_path: Path):
    """Analyze a single artwork and return listing data without file I/O."""
    logger.info(f"--- Starting analysis for: {image_path.name} (User: {USER_ID}) ---")
    _write_status("Starting analysis...", 5, image_path.name)

    if not image_path.is_file():
        raise FileNotFoundError(f"Input image not found: {image_path}")

    sku = image_path.parent.name
    aspect = get_aspect_ratio(image_path)

    start_time = _dt.datetime.now(_dt.timezone.utc)
    _write_status("Calling OpenAI API...", 40, image_path.name)
    ai_listing, raw_response = generate_ai_listing(image_path, aspect, sku)

    orig_path = image_path.parent / f"{sku}-original.jpg"
    primary_colour, secondary_colour = get_dominant_colours(orig_path, 2)
    final_description = ai_listing.get("description") or assemble_gdws_description(aspect)
    end_time = _dt.datetime.now(_dt.timezone.utc)

    listing_data = {
        "filename": orig_path.name,
        "aspect_ratio": aspect,
        "sku": sku,
        "title": ai_listing.get("title", image_path.stem),
        "description": final_description,
        "tags": ai_listing.get("tags", []),
        "materials": ai_listing.get("materials", []),
        "primary_colour": primary_colour,
        "secondary_colour": secondary_colour,
        "price": ai_listing.get("price", 18.27),
        "seo_filename": ai_listing.get("seo_filename", ai_listing.get("seo_filename_slug")),
        "openai_analysis": {
            "optimized_file": str(image_path),
            "time_sent": start_time.isoformat(),
            "time_responded": end_time.isoformat(),
            "status": "success",
            "api_response": raw_response[:500] + "..." if raw_response else "N/A",
        },
    }

    logger.info(f"--- Successfully completed analysis for: {image_path.name} ---")
    return {"listing": listing_data, "aspect_ratio": aspect, "sku": sku}

# ===========================================================================
# 8. Command-Line Interface (CLI)
# ===========================================================================

def main():
    """Parses CLI arguments and runs the analysis."""
    parser = argparse.ArgumentParser(description="Analyze artwork(s) with OpenAI.")
    parser.add_argument("image", help="Path to a single image file to process.")
    parser.add_argument("--json-output", action="store_true", help="Emit result as JSON for subprocess integration.")
    parser.add_argument("--provider", help="Ignored, for compatibility.")
    args = parser.parse_args()

    try:
        result = analyze_single(Path(args.image))
        if args.json_output:
            print(json.dumps(result, indent=2))
        else:
            listing = result.get("listing", {})
            print(
                f"\n✅ Analysis complete for: {args.image}\n   - Title: {listing.get('title')}\n   - SKU: {result.get('sku')}"
            )

    except Exception as e:
        logger.critical(f"A fatal error occurred during analysis: {e}\n{traceback.format_exc()}")
        if args.json_output:
            print(json.dumps({"success": False, "error": str(e)}), file=sys.stderr)
            sys.exit(1)
        else:
            print(f"\n❌ An error occurred: {e}")
            print(f"   Please check the latest log file for details.")


if __name__ == "__main__":
    main()