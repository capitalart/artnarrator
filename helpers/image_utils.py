from __future__ import annotations
import importlib
from pathlib import Path
from typing import Tuple
import os
from PIL import Image

try:
    pyvips = importlib.import_module("pyvips")
except Exception:
    pyvips = None


def _ensure_out_dir(d: Path) -> None:
    d.mkdir(parents=True, exist_ok=True)


def make_working_copy(src_path: Path, out_dir: Path, long_edge: int = 6000, quality: int = 90) -> Path:
    """Create an optimized JPEG working copy of the source image.

    - Tries to use pyvips (libvips) for a low-memory fast path when available.
    - Falls back to Pillow when pyvips is not present.
    - Returns the Path to the new working copy (JPEG).
    """
    _ensure_out_dir(out_dir)
    out_path = out_dir / f"{src_path.stem}-optimized.jpg"
    # Remove stale file first
    if out_path.exists():
        try:
            out_path.unlink()
        except Exception:
            pass

    if pyvips:
        try:
            # Use thumbnail_image to limit the long edge while keeping aspect
            image = pyvips.Image.new_from_file(str(src_path), access="sequential")
            # If image is already small, write as-is (but converted to JPEG)
            if max(image.width, image.height) <= long_edge:
                image.write_to_file(str(out_path), Q=quality)
            else:
                thumb = image.thumbnail_image(long_edge)
                thumb.write_to_file(str(out_path), Q=quality)
            return out_path
        except Exception:
            # Fall through to Pillow
            pass

    # Pillow fallback (memory heavier but safe for moderate sizes)
    with Image.open(src_path) as im:
        im = im.convert("RGB")
        im.thumbnail((long_edge, long_edge), Image.LANCZOS)
        im.save(out_path, "JPEG", quality=quality, optimize=True)
    return out_path


def get_image_dimensions(path: Path) -> Tuple[int, int]:
    """Return (width, height) for an image path without loading whole image into memory where possible."""
    if pyvips:
        try:
            img = pyvips.Image.new_from_file(str(path), access='sequential')
            return img.width, img.height
        except Exception:
            pass
    with Image.open(path) as im:
        return im.size


def ensure_max_filesize(path: Path, max_mb: int) -> bool:
    """Return True if file size is <= max_mb, else False."""
    try:
        return path.stat().st_size <= max_mb * 1024 * 1024
    except Exception:
        return False
