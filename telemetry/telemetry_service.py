#!/usr/bin/env python3
"""
Telemetry sidecar service for Analysis Pipeline.

- POST /event        -> accepts JSON events (one per POST), appends to JSONL log
- GET  /health       -> returns 200 OK
- GET  /events?limit=200 -> returns the last N events as JSON array

Writes: logs/analysis-events.jsonl  (one JSON object per line)
Safe: if parent app is down, this still runs; if this is down, client falls back to local spill file.
"""
from __future__ import annotations
import json, os, threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List
from flask import Flask, request, jsonify

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parents[1]
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)
EVENTS_PATH = LOGS_DIR / "analysis-events.jsonl"
_write_lock = threading.Lock()

def utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def append_event(ev: Dict[str, Any]) -> None:
    ev.setdefault("ts", utc_iso())
    line = json.dumps(ev, ensure_ascii=False)
    with _write_lock:
        with EVENTS_PATH.open("a", encoding="utf-8") as f:
            f.write(line + "\n")

@app.route("/health")
def health():
    return "OK", 200

@app.route("/event", methods=["POST"])
def event():
    try:
        ev = request.get_json(force=True, silent=False) or {}
        ev.setdefault("event", "unknown")
        ev.setdefault("source", "unknown")
        ev.setdefault("version", 1)
        append_event(ev)
        return jsonify({"ok": True}), 200
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 400

@app.route("/events")
def events():
    try:
        limit = int(request.args.get("limit", "200"))
        limit = max(1, min(limit, 5000))
        lines: List[str] = []
        if EVENTS_PATH.exists():
            with EVENTS_PATH.open("rb") as f:
                f.seek(0, os.SEEK_END)
                size = f.tell()
                block = 8192
                data = b""
                while len(lines) <= limit and size > 0:
                    step = min(block, size)
                    size -= step
                    f.seek(size)
                    data = f.read(step) + data
                    lines = data.splitlines()
        objs = []
        for b in lines[-limit:]:
            try:
                objs.append(json.loads(b.decode("utf-8") if isinstance(b, (bytes, bytearray)) else b))
            except Exception:
                continue
        return jsonify(objs), 200
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5055)
