# tests/_session_cleaner.py
from __future__ import annotations
import json, os, shutil, sys, tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, List

def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]

def _read_json_safely(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None

def _atomic_write_text(p: Path, data: str) -> None:
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(data, encoding="utf-8")
    tmp.replace(p)

def _atomic_write_json(p: Path, obj: Any) -> None:
    _atomic_write_text(p, json.dumps(obj, ensure_ascii=False, indent=2))

def _rmtree(path: Path) -> None:
    def _onerror(func, func_path, exc_info):
        try:
            os.chmod(func_path, 0o700)
            func(func_path)
        except Exception:
            pass
    if path.exists():
        shutil.rmtree(path, onerror=_onerror)

def _list_subdirs(d: Path) -> List[str]:
    if not d.exists():
        return []
    return sorted([p.name for p in d.iterdir() if p.is_dir()])

def _resolve_paths_from_env(env_key: str, base: Path) -> List[Path]:
    raw = os.getenv(env_key, "").strip()
    if not raw:
        return []
    items = [s.strip() for s in raw.split(",") if s.strip()]
    out: List[Path] = []
    for s in items:
        p = Path(s)
        out.append(p if p.is_absolute() else (base / p))
    return out

def _is_under(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except Exception:
        return False

@contextmanager
def session_cleaner_context(stdout_logger=print):
    repo = _repo_root()
    art_processing = repo / "art-processing"
    master_json = art_processing / "master-artwork-paths.json"
    pending_json = art_processing / "pending_mockups.json"
    processed_dir = art_processing / "processed-artwork"

    extra_paths = _resolve_paths_from_env("TEST_SNAPSHOT_PATHS", repo)
    strict = os.getenv("STRICT_TEARDOWN", "").lower() in {"1", "true", "yes"}
    keep_artifacts = os.getenv("KEEP_TEST_ARTIFACTS", "").lower() in {"1", "true", "yes"}

    baseline: Dict[str, Any] = {
        "master_present": master_json.exists(),
        "master_json": _read_json_safely(master_json) if master_json.exists() else None,
        "pending_present": pending_json.exists(),
        "pending_json": _read_json_safely(pending_json) if pending_json.exists() else None,
        "processed_present": processed_dir.exists(),
        "processed_subdirs": _list_subdirs(processed_dir),
        "extra": {},
    }

    for p in extra_paths:
        if p.exists():
            if p.is_dir():
                baseline["extra"][str(p)] = {
                    "type": "dir",
                    "present": True,
                    "children": sorted([c.name for c in p.iterdir()]),
                }
            else:
                baseline["extra"][str(p)] = {
                    "type": "file",
                    "present": True,
                    "bytes": p.read_bytes(),
                }
        else:
            baseline["extra"][str(p)] = {"type": ("dir" if p.suffix == "" else "file"), "present": False}

    stdout_logger("[session_files_cleanup] Snapshot complete")
    try:
        yield
    finally:
        actions, failures = [], []

        def _log_action(msg: str):
            actions.append(msg)
            stdout_logger(f"[session_files_cleanup] {msg}")

        def _log_fail(msg: str):
            failures.append(msg)
            stdout_logger(f"[session_files_cleanup][FAIL] {msg}")

        try:
            if keep_artifacts:
                _log_action("KEEP_TEST_ARTIFACTS=1 set — skipping teardown.")
            else:
                # master
                if baseline["master_present"]:
                    try:
                        _atomic_write_json(master_json, baseline["master_json"])
                        _log_action(f"restored {master_json}")
                    except Exception as e:
                        _log_fail(f"restore {master_json}: {e}")
                else:
                    if master_json.exists():
                        try:
                            master_json.unlink()
                            _log_action(f"deleted {master_json}")
                        except Exception as e:
                            _log_fail(f"delete {master_json}: {e}")

                # pending (sanitize if no baseline)
                tmp_root = Path(tempfile.gettempdir())

                def sanitize_pending_list(lst: List[str]) -> List[str]:
                    out: List[str] = []
                    for s in lst:
                        p = Path(s)
                        if _is_under(p, tmp_root):
                            continue
                        if "pytest-of-" in s:
                            continue
                        if not _is_under(p, processed_dir):
                            continue
                        if not p.exists():
                            continue
                        out.append(str(p))
                    return out

                if baseline["pending_present"]:
                    try:
                        _atomic_write_json(pending_json, baseline["pending_json"])
                        _log_action(f"restored {pending_json}")
                    except Exception as e:
                        _log_fail(f"restore {pending_json}: {e}")
                else:
                    if pending_json.exists():
                        try:
                            current = _read_json_safely(pending_json) or []
                            if not isinstance(current, list):
                                current = []
                            filtered = sanitize_pending_list(current)
                            if filtered:
                                _atomic_write_json(pending_json, filtered)
                                _log_action(f"sanitized {pending_json} (kept {len(filtered)}, removed {len(current)-len(filtered)})")
                            else:
                                pending_json.unlink()
                                _log_action(f"deleted {pending_json} (no baseline and no valid entries)")
                        except Exception as e:
                            _log_fail(f"sanitize/delete {pending_json}: {e}")

                # processed subdirs
                if processed_dir.exists():
                    current = set(_list_subdirs(processed_dir))
                    baseline_set = set(baseline["processed_subdirs"])
                    for name in sorted(current - baseline_set):
                        target = processed_dir / name
                        try:
                            _rmtree(target)
                            _log_action(f"rmtree {target}")
                        except Exception as e:
                            _log_fail(f"rmtree {target}: {e}")
                else:
                    if baseline["processed_present"] is False and processed_dir.exists():
                        try:
                            _rmtree(processed_dir)
                            _log_action(f"rmtree {processed_dir}")
                        except Exception as e:
                            _log_fail(f"rmtree {processed_dir}: {e}")

                # extra paths
                for s, meta in baseline["extra"].items():
                    p = Path(s)
                    was_present = meta["present"]
                    if meta["type"] == "file":
                        if was_present:
                            try:
                                b = meta.get("bytes", b"")
                                if isinstance(b, bytes):
                                    p.write_bytes(b)
                                else:
                                    _atomic_write_text(p, str(b))
                                _log_action(f"restored file {p}")
                            except Exception as e:
                                _log_fail(f"restore file {p}: {e}")
                        else:
                            if p.exists():
                                try:
                                    p.unlink()
                                    _log_action(f"deleted file {p}")
                                except Exception as e:
                                    _log_fail(f"delete file {p}: {e}")
                    else:
                        if was_present:
                            try:
                                baseline_children = set(meta.get("children", []))
                                if p.exists():
                                    for child in p.iterdir():
                                        if child.name not in baseline_children:
                                            if child.is_dir():
                                                _rmtree(child)
                                                _log_action(f"rmtree {child}")
                                            else:
                                                child.unlink(missing_ok=True)
                                                _log_action(f"deleted file {child}")
                            except Exception as e:
                                _log_fail(f"prune dir {p}: {e}")
                        else:
                            if p.exists():
                                try:
                                    _rmtree(p)
                                    _log_action(f"rmtree dir {p}")
                                except Exception as e:
                                    _log_fail(f"rmtree dir {p}: {e}")
        finally:
            if failures and strict:
                raise RuntimeError(
                    "Session teardown reported cleanup failures:\n- " + "\n- ".join(failures)
                )
