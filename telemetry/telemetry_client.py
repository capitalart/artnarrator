"""
Lightweight client to emit telemetry events to the sidecar.
- Non-blocking (short timeouts); never raises to callers.
- Falls back to logs/analysis-events.spool.jsonl if service is down.
- No external deps: uses urllib from stdlib.
"""
from __future__ import annotations
import json, os
from pathlib import Path
from typing import Any, Dict
from urllib.request import Request, urlopen

BASE_DIR = Path(__file__).resolve().parents[1]
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)
SPILL_PATH = LOGS_DIR / "analysis-events.spool.jsonl"

TELEMETRY_URL = os.getenv("TELEMETRY_URL", "http://127.0.0.1:5055/event")
APP_NAME = os.getenv("APP_NAME", "artnarrator")

def _spill(ev: Dict[str, Any]) -> None:
    try:
        with SPILL_PATH.open("a", encoding="utf-8") as f:
            f.write(json.dumps(ev, ensure_ascii=False) + "\n")
    except Exception:
        pass

def emit(event: str, **fields: Any) -> None:
    try:
        body = {"event": event, "source": APP_NAME, "version": 1, **fields}
        data = json.dumps(body).encode("utf-8")
        req = Request(TELEMETRY_URL, data=data, headers={"Content-Type": "application/json"}, method="POST")
        with urlopen(req, timeout=0.3) as resp:
            resp.read(0)
    except Exception:
        _spill(body)
