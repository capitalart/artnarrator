#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyze artwork (SKU-first or file path) and, on success, commit a processed
folder + listing JSON. In production, requires real OpenAI output before writing.

Modes
-----
- PROD (ENVIRONMENT=prod and USE_STUB_ANALYSIS=0):
    * Calls OpenAI. If no usable AI output, exits non-zero and writes nothing.
- DEV/TEST (ENVIRONMENT!=prod or USE_STUB_ANALYSIS=1):
    * Uses stub listing so tests don't hit the network.

CLI
---
python scripts/analyze_artwork.py RJC-0509 --json-output
python scripts/analyze_artwork.py art-processing/unanalysed-artwork/RJC-0509/RJC-0509-analyse.jpg --json-output
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import os
import shutil
import sys
import traceback
from pathlib import Path
from typing import Any, Dict, Tuple, Optional

# Ensure repo root on path for local imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config
from utils.logger_utils import setup_logger
from helpers.image_utils import make_working_copy, get_image_dimensions
from helpers.listing_utils import assemble_gdws_description
from utils.sku_assigner import get_next_sku

# ------------------------------------------------------------------------------
# Logger (writes to logs/ANALYZE_SCRIPT/*.log)
# ------------------------------------------------------------------------------
logger = setup_logger("analyze_artwork_script", "ANALYZE_SCRIPT")

# ------------------------------------------------------------------------------
# Compatibility shim for tests that monkeypatch `aa.client.chat.completions.create`
# ------------------------------------------------------------------------------
class _DummyCompletions:
    def create(self, *args, **kwargs):
        raise NotImplementedError("OpenAI client not configured")

class _DummyChat:
    def __init__(self):
        self.completions = _DummyCompletions()

class _DummyClient:
    def __init__(self):
        self.chat = _DummyChat()

# This stays importable as `aa.client` in tests
client = _DummyClient()

# ------------------------------------------------------------------------------
# Env switches
# ------------------------------------------------------------------------------
ENVIRONMENT = os.getenv("ENVIRONMENT", getattr(config, "ENVIRONMENT", "dev"))
USE_STUB_ANALYSIS = os.getenv("USE_STUB_ANALYSIS", "0") == "1"
STRICT_ANALYZE = os.getenv("STRICT_ANALYZE", "1" if ENVIRONMENT == "prod" else "0") == "1"
ANALYZE_PROVIDER = os.getenv("ANALYZE_PROVIDER", "openai").lower().strip() or "openai"

# ------------------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------------------
def _write_status(step: str, percent: int, filename: str) -> None:
    try:
        config.ANALYSIS_STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
        config.ANALYSIS_STATUS_FILE.write_text(
            json.dumps({"step": step, "percent": percent, "file": filename}),
            encoding="utf-8",
        )
    except Exception:
        logger.debug("Could not write analysis status file.", exc_info=True)

def get_aspect_ratio(image_path: Path) -> str:
    try:
        w, h = get_image_dimensions(image_path)
    except Exception:
        w, h = (1, 1)
    aspect_map = [
        ("1x1", 1/1), ("2x3", 2/3), ("3x2", 3/2), ("3x4", 3/4),
        ("4x3", 4/3), ("4x5", 4/5), ("5x4", 5/4), ("5x7", 5/7),
        ("7x5", 7/5), ("9x16", 9/16), ("16x9", 16/9),
    ]
    ar = (w / h) if h else 1.0
    best = min(aspect_map, key=lambda tup: abs(ar - tup[1]))
    return best[0]

def create_seo_filename(slug: str, sku: str) -> str:
    safe = "".join(c if (c.isalnum() or c == "-") else "-" for c in slug).strip("-")
    base = f"{safe}-by-robin-custance-rjc-{sku}".lower()
    if len(base) > 70:
        base = base[:70]
    return f"{base}.jpg"

def get_dominant_colours(img_path: Path, n: int = 2) -> list[str]:
    """Very light pseudo-dominant colours detector."""
    try:
        temp_dir = config.UNANALYSED_ROOT / "temp"
        temp_dir.mkdir(parents=True, exist_ok=True)
        opt = make_working_copy(img_path, temp_dir, long_edge=300, quality=85)
        from PIL import Image
        with Image.open(opt) as im:
            im = im.convert("RGB").resize((50, 50))
            pixels = list(im.getdata())
        # (We could compute averages; keep simple placeholders for now.)
        return ["White", "Black"][:n]
    except Exception:
        return ["White", "Black"][:n]

def add_to_mockup_queue(artwork_path: str) -> bool:
    try:
        qfile = config.PENDING_MOCKUPS_QUEUE_FILE
        qfile.parent.mkdir(parents=True, exist_ok=True)
        current = []
        if qfile.exists():
            try:
                current = json.loads(qfile.read_text(encoding="utf-8"))
            except Exception:
                current = []
        if str(artwork_path) not in current:
            current.append(str(artwork_path))
        qfile.write_text(json.dumps(current, indent=2), encoding="utf-8")
        logger.info("Queued mockup generation for: %s", artwork_path)
        return True
    except Exception:
        logger.exception("Failed to queue mockup")
        return False

# ------------------------------------------------------------------------------
# AI listing producers (real vs stub)
# ------------------------------------------------------------------------------
def _stub_listing(image_path: Path, aspect: str, assigned_sku: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Returns (listing_fields, meta) for dev/test."""
    title = f"Artwork {assigned_sku}"
    listing = {
        "title": title,
        "description": assemble_gdws_description(aspect),  # generic block
        "tags": [],
        "materials": [],
        "price": 18.27,
        "seo_filename_slug": title.replace(" ", "-")[:60],
    }
    meta = {"provider": "stub", "openai_analysis": {}}  # empty -> will fail strict gate in prod
    return listing, meta

def _openai_listing(image_path: Path, aspect: str, assigned_sku: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Returns (listing_fields, meta) using OpenAI.
    meta.openai_analysis.text must be non-empty for STRICT gate to pass.
    """
    try:
        # Prefer your centralised client if present (keeps auth/config in one place)
        from utils.ai_services import get_openai_client
        oai = get_openai_client()
    except Exception:
        oai = None

    # Fallback: support tests that patch aa.client.chat.completions.create
    patched_chat = getattr(getattr(client, "chat", None), "completions", None)

    if oai is None and patched_chat is None:
        raise RuntimeError("OpenAI client not available")

    prompt = (
        "You are generating a product listing for fine art wall print.\n"
        f"- Aspect: {aspect}\n"
        f"- SKU: {assigned_sku}\n"
        "Return a concise JSON with keys: title, description (450-700 words), tags (<=13 array), materials (<=5 array).\n"
    )

    # Minimal model/endpoint handling (supports classic chat.completions OR responses)
    text_out = ""
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    try:
        if oai is not None:
            # Newer SDKs expose client.chat.completions.create or client.responses.create
            create_chat = getattr(getattr(oai, "chat", None), "completions", None)
            if create_chat and hasattr(create_chat, "create"):
                resp = create_chat.create(model=model, messages=[{"role": "user", "content": prompt}])
                text_out = resp.choices[0].message.content if resp and resp.choices else ""
            else:
                # try responses.create
                create_resp = getattr(oai, "responses", None)
                if create_resp and hasattr(create_resp, "create"):
                    r = create_resp.create(model=model, input=prompt)
                    # try common fields
                    text_out = getattr(r, "output_text", None) or getattr(r, "text", None) or ""
        elif patched_chat and hasattr(patched_chat, "create"):
            resp = patched_chat.create(model=model, messages=[{"role": "user", "content": prompt}])
            text_out = getattr(resp.choices[0].message, "content", "")
    except Exception as e:
        logger.error("OpenAI call failed: %s", e, exc_info=True)
        raise

    if not (text_out and text_out.strip()):
        raise RuntimeError("OpenAI returned no content")

    # Heuristic parse: try to extract a JSON block or fall back to text shaping
    title = f"Artwork {assigned_sku}"
    desc = text_out.strip()
    tags, materials = [], []
    try:
        import re, json as _json
        m = re.search(r"\{.*\}", text_out, re.S)  # crude
        if m:
            obj = _json.loads(m.group(0))
            title = (obj.get("title") or title).strip()[:140]
            desc = (obj.get("description") or desc).strip()
            tags = obj.get("tags") or []
            materials = obj.get("materials") or []
    except Exception:
        pass

    listing = {
        "title": title,
        "description": desc,
        "tags": tags[:13],
        "materials": materials[:5],
        "price": 18.27,
        "seo_filename_slug": (title or f"art-{assigned_sku}").replace(" ", "-")[:60],
    }
    meta = {
        "provider": "openai",
        "openai_analysis": {
            "model": model,
            "text": desc[:2000],
            "ts": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        },
    }
    return listing, meta

def _is_ai_sufficient(listing: Dict[str, Any], meta: Dict[str, Any]) -> bool:
    """
    Strict gate for production: only allow commit if we have real AI content.
    Rule: meta.openai_analysis.text must be non-empty (not stubbed).
    Adjust if you want stronger checks.
    """
    try:
        text = (meta.get("openai_analysis", {}) or {}).get("text", "")
        title_ok = bool((listing.get("title") or "").strip())
        return title_ok and bool(text and text.strip())
    except Exception:
        return False

# ------------------------------------------------------------------------------
# Core flows
# ------------------------------------------------------------------------------
def _finalize_commit(
    sku: str,
    aspect: str,
    orig_source: Path,
    ai_listing: Dict[str, Any],
    meta: Dict[str, Any],
    qc_data: Dict[str, Any],
) -> Dict[str, Any]:
    """Create processed folder, copy image, write listing, queue mockups."""
    seo_slug_candidate = ai_listing.get("seo_filename_slug") or ai_listing.get("title", sku).replace(" ", "-")
    seo_filename = create_seo_filename(seo_slug_candidate, sku)
    seo_folder = Path(seo_filename).stem
    processed_folder = config.PROCESSED_ROOT / seo_folder
    processed_folder.mkdir(parents=True, exist_ok=True)

    final_image_path = processed_folder / seo_filename
    try:
        shutil.copy2(str(orig_source), str(final_image_path))
    except Exception:
        # As last resort, make an empty placeholder file to avoid 404s (optional)
        final_image_path.write_bytes(b"")

    primary, secondary = get_dominant_colours(orig_source, 2)

    full_listing: Dict[str, Any] = {}
    full_listing.update(qc_data or {})
    full_listing.update(ai_listing or {})
    full_listing.update({
        "sku": sku,
        "seo_filename": seo_filename,
        "aspect_ratio": aspect,
        "primary_colour": primary,
        "secondary_colour": secondary,
    })
    # keep the meta (provider + openai_analysis) for auditing
    full_listing.update(meta or {})

    listing_path = processed_folder / f"{seo_folder}-listing.json"
    listing_path.write_text(json.dumps(full_listing, indent=2, ensure_ascii=False), encoding="utf-8")

    try:
        add_to_mockup_queue(str(processed_folder))
    except Exception:
        logger.exception("Failed to append to mockup queue")

    # Best-effort: remove the unanalysed SKU dir now that we committed
    try:
        unan = config.UNANALYSED_ROOT / sku
        if unan.exists():
            shutil.rmtree(unan)
    except Exception:
        logger.exception("Failed to remove unanalysed dir")

    return {
        "success": True,
        "sku": sku,
        "processed_folder": str(processed_folder),
        "listing": full_listing,
    }

def analyze_single(image_path: Path) -> Dict[str, Any]:
    """Legacy path input (rare): resolve SKU from parent folder if possible."""
    _write_status("starting", 0, image_path.name)

    parent_name = image_path.parent.name
    sku = parent_name if str(parent_name).upper().startswith(config.SKU_CONFIG["PREFIX"]) else get_next_sku(config.SKU_TRACKER)
    aspect = get_aspect_ratio(image_path)

    # choose source (try a better original if present)
    orig = image_path
    candidate = image_path.parent / f"{sku}-original.jpg"
    if candidate.exists():
        orig = candidate
    else:
        src = image_path.parent / f"{sku}-source.jpg"
        if src.exists():
            orig = src

    # choose AI path
    if ENVIRONMENT == "prod" and not USE_STUB_ANALYSIS and ANALYZE_PROVIDER == "openai":
        ai_listing, meta = _openai_listing(image_path, aspect, sku)
        if STRICT_ANALYZE and not _is_ai_sufficient(ai_listing, meta):
            raise RuntimeError("Strict analyze: OpenAI output insufficient; aborting without writing.")
    else:
        ai_listing, meta = _stub_listing(image_path, aspect, sku)

    # QC if present
    qc = image_path.parent / f"{sku}.qc.json"
    qc_data: Dict[str, Any] = {}
    if qc.exists():
        try:
            qc_data = json.loads(qc.read_text(encoding="utf-8"))
        except Exception:
            qc_data = {}

    return _finalize_commit(sku, aspect, orig, ai_listing, meta, qc_data)

def process_sku(sku: str, json_output: bool = False) -> Dict[str, Any]:
    """Preferred SKU-first flow."""
    unan = config.UNANALYSED_ROOT / sku
    if not unan.exists():
        raise FileNotFoundError(f"Unanalysed folder not found for SKU: {sku}")

    analyse = unan / f"{sku}-analyse.jpg"
    source = unan / f"{sku}-source.jpg"
    if not analyse.exists() or not source.exists():
        raise FileNotFoundError("Required files missing in unanalysed folder")

    aspect = get_aspect_ratio(analyse)

    # choose AI path
    if ENVIRONMENT == "prod" and not USE_STUB_ANALYSIS and ANALYZE_PROVIDER == "openai":
        ai_listing, meta = _openai_listing(analyse, aspect, sku)
        if STRICT_ANALYZE and not _is_ai_sufficient(ai_listing, meta):
            raise RuntimeError("Strict analyze: OpenAI output insufficient; aborting without writing.")
    else:
        ai_listing, meta = _stub_listing(analyse, aspect, sku)

    # QC
    qc = unan / f"{sku}.qc.json"
    qc_data: Dict[str, Any] = {}
    if qc.exists():
        try:
            qc_data = json.loads(qc.read_text(encoding="utf-8"))
        except Exception:
            qc_data = {}

    return _finalize_commit(sku, aspect, source, ai_listing, meta, qc_data)

# ------------------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Analyze artwork by SKU or by image path (legacy).")
    parser.add_argument("input", help="SKU (preferred) or path to image file for legacy mode.")
    parser.add_argument("--json-output", action="store_true", help="Emit result as JSON for subprocess integration.")
    args = parser.parse_args()

    try:
        if str(args.input).upper().startswith(config.SKU_CONFIG["PREFIX"]):
            result = process_sku(str(args.input), json_output=args.json_output)
        else:
            result = analyze_single(Path(args.input))

        if args.json_output:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        logger.critical("Fatal analysis error: %s\n%s", e, traceback.format_exc())
        if args.json_output:
            print(json.dumps({"success": False, "error": str(e)}), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
