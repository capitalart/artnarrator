# conftest.py
# =============================================================================
# Test configuration and fixtures for ArtNarrator / DreamArtMachine
# - Session-wide snapshot/cleanup (autouse) via tests._session_cleaner.session_cleaner_context
# - Pytest hooks for "live" tests gating
# - Isolated filesystem per test (managed_artwork_paths)
# - Test Flask client with patched config + session cleanup
# - Subprocess stubs to prevent real background/CLI execution
# =============================================================================

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

# Make repo root importable
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

# App / config
import config  # noqa: E402
from app import app as flask_app  # noqa: E402

# Robust session snapshot/restore helper (also sanitizes pending_mockups.json)
from tests._session_cleaner import session_cleaner_context  # noqa: E402


# =============================================================================
# SECTION 0: SESSION SNAPSHOT / CLEANUP (AUTO-USE)
# =============================================================================

@pytest.fixture(scope="session", autouse=True)
def session_files_cleanup():
    """
    Autouse, session-scoped fixture that wraps the robust snapshot/restore context.
    - Restores master-artwork-paths.json and pending_mockups.json (or deletes if created by tests)
    - Removes processed-artwork subfolders created by tests
    - Sanitizes pending_mockups.json to drop /tmp/pytest-of-* and dead paths
    - Honors env flags: STRICT_TEARDOWN, KEEP_TEST_ARTIFACTS, TEST_SNAPSHOT_PATHS
    """
    with session_cleaner_context():
        yield


# =============================================================================
# SECTION 1: PYTEST HOOKS
# =============================================================================

def pytest_addoption(parser):
    parser.addoption(
        "--run-live-tests",
        action="store_true",
        default=False,
        help="run live API tests that hit real services / filesystem",
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "live: marks tests as live (skipped by default)")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-live-tests"):
        return
    skip_live = pytest.mark.skip(reason="need --run-live-tests option to run")
    for item in items:
        if "live" in item.keywords:
            item.add_marker(skip_live)


# =============================================================================
# SECTION 2: ISOLATED FILESYSTEM FIXTURES
# =============================================================================

@pytest.fixture
def managed_artwork_paths(tmp_path_factory):
    """
    Creates a temporary, isolated directory structure for each test function.

    Layout:
      <tmp>/art_processing/
        ├─ unanalysed-artwork/
        └─ processed-artwork/
    """
    base_dir = tmp_path_factory.mktemp("art_processing")
    paths = {
        "base": base_dir,
        "unanalysed": base_dir / "unanalysed-artwork",
        "processed": base_dir / "processed-artwork",
    }
    paths["unanalysed"].mkdir(parents=True, exist_ok=True)
    paths["processed"].mkdir(parents=True, exist_ok=True)
    yield SimpleNamespace(**paths)


# =============================================================================
# SECTION 3: FLASK TEST CLIENT (PATCHED CONFIG)
# =============================================================================

@pytest.fixture
def client(managed_artwork_paths, monkeypatch):
    """
    Master fixture: returns a Flask test client with config patched to the
    per-test temp filesystem. Ensures tests run in 'dev' environment so the
    session eviction utility is permitted.
    """
    # Patch config used by the app
    monkeypatch.setattr(config, "BASE_DIR", managed_artwork_paths.base)
    monkeypatch.setattr(config, "UNANALYSED_ROOT", managed_artwork_paths.unanalysed)
    monkeypatch.setattr(config, "PROCESSED_ROOT", managed_artwork_paths.processed)
    monkeypatch.setattr(config, "ENVIRONMENT", "dev")

    # Mirror into Flask config (if the app consults flask_app.config)
    flask_app.config.update(
        TESTING=True,
        BASE_DIR=managed_artwork_paths.base,
        UNANALYSED_ROOT=managed_artwork_paths.unanalysed,
        PROCESSED_ROOT=managed_artwork_paths.processed,
    )

    # Provide a safe default for ANALYZE_SCRIPT_PATH if not set by config
    if not hasattr(config, "ANALYZE_SCRIPT_PATH"):
        monkeypatch.setattr(config, "ANALYZE_SCRIPT_PATH", REPO_ROOT / "scripts" / "analyze_artwork.py")

    with flask_app.test_client() as test_client:
        # Try to clear any pre-existing sessions for the test user
        try:
            from utils import session_tracker as _st  # type: ignore
            for s in _st.active_sessions("robbie"):
                _st.remove_session("robbie", s["session_id"])
        except Exception:
            # No session tracker or nothing to clear — safe to continue
            pass

        # Perform a test login (ignore failures silently; routes may vary between branches)
        try:
            test_client.post(
                "/login",
                data={"username": "robbie", "password": "kangaroo123"},
                follow_redirects=True,
            )
        except Exception:
            pass

        yield test_client


# =============================================================================
# SECTION 4: SUBPROCESS STUBS (PREVENT REAL BACKGROUND WORK)
# =============================================================================

@pytest.fixture
def prevent_background_processes(monkeypatch, managed_artwork_paths):
    """
    Prevents tests from launching real background subprocesses and provides
    predictable fake outputs for analysis calls.

    Stubs:
      - subprocess.Popen   -> _DummyPopen
      - subprocess.run     -> _fake_run

    Behavior for analyze CLI:
      - Creates a processed folder under the test's processed root
      - Writes <seo>-listing.json and a tiny .jpg
      - Returns JSON payload on stdout consistent with the app's expectations
    """

    class _DummyPopen:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.returncode = 0

        def poll(self):
            return self.returncode

        def wait(self, timeout=None):
            return self.returncode

        def kill(self):
            pass

        def communicate(self, input=None, timeout=None):
            cmd = self.args[0]
            try:
                script_part = cmd[1] if len(cmd) > 1 else ""
            except Exception:
                script_part = ""

            if "analyze_artwork.py" in str(script_part):
                img_arg = Path(cmd[2]) if len(cmd) > 2 else None
                if img_arg and img_arg.exists() and img_arg.is_file():
                    seo_name = f"mocked-artwork-from-{img_arg.stem}-by-test-RJC-MOCK"
                else:
                    # If not given a file, derive a name from the arg itself
                    fallback = str(cmd[2]) if len(cmd) > 2 else "mocked-artwork"
                    seo_name = Path(fallback).stem or "mocked-artwork"

                processed_dir = managed_artwork_paths.processed / seo_name
                processed_dir.mkdir(parents=True, exist_ok=True)

                # Ensure there's a file in the dir (copy source or write tiny jpg)
                if img_arg and img_arg.exists() and img_arg.is_file():
                    try:
                        shutil.copy(img_arg, processed_dir / f"{seo_name}.jpg")
                    except Exception:
                        (processed_dir / f"{seo_name}.jpg").write_bytes(b"\xff\xd8\xff\xd9")
                else:
                    (processed_dir / f"{seo_name}.jpg").write_bytes(b"\xff\xd8\xff\xd9")

                listing_data = {
                    "title": "Mocked Title",
                    "seo_filename": f"{seo_name}.jpg",
                    "aspect_ratio": "4x5",
                }
                (processed_dir / f"{seo_name}-listing.json").write_text(
                    json.dumps(listing_data), encoding="utf-8"
                )

                payload = {
                    "success": True,
                    "processed_folder": str(processed_dir),
                    "listing": listing_data,
                    "sku": "RJC-MOCK-01",
                }
                return (json.dumps(payload).encode("utf-8"), b"")
            return (b"", b"")

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    monkeypatch.setattr(subprocess, "Popen", _DummyPopen)

    class _FakeCompletedProcess:
        def __init__(self, returncode=0, stdout=b"", stderr=b""):
            self.returncode = returncode
            self.stdout = stdout
            self.stderr = stderr

    def _fake_run(cmd, capture_output=True, text=True, cwd=None, timeout=None, check=False):
        # Determine "analyze" invocation robustly
        analyze_script = getattr(config, "ANALYZE_SCRIPT_PATH", REPO_ROOT / "scripts" / "analyze_artwork.py")
        script_str = ""
        try:
            script_str = str(cmd[1])
        except Exception:
            pass

        looks_like_analyze = "analyze_artwork.py" in script_str or str(analyze_script) in script_str

        if looks_like_analyze:
            target = cmd[2] if len(cmd) > 2 else None
            P = Path
            if target:
                tgt = P(target)
                if tgt.exists() and tgt.is_file():
                    seo_name = f"mocked-artwork-from-{tgt.stem}-by-test-RJC-MOCK"
                    processed_dir = managed_artwork_paths.processed / seo_name
                    processed_dir.mkdir(parents=True, exist_ok=True)
                    try:
                        shutil.copy(tgt, processed_dir / f"{seo_name}.jpg")
                    except Exception:
                        (processed_dir / f"{seo_name}.jpg").write_bytes(b"\xff\xd8\xff\xd9")
                else:
                    # Treat target as folder/sku name
                    seo_name = P(str(target)).stem or "mocked-artwork"
                    processed_dir = managed_artwork_paths.processed / seo_name
                    processed_dir.mkdir(parents=True, exist_ok=True)
                    (processed_dir / f"{seo_name}.jpg").write_bytes(b"\xff\xd8\xff\xd9")
            else:
                seo_name = "mocked-artwork"
                processed_dir = managed_artwork_paths.processed / seo_name
                processed_dir.mkdir(parents=True, exist_ok=True)
                (processed_dir / f"{seo_name}.jpg").write_bytes(b"\xff\xd8\xff\xd9")

            listing = {
                "title": "Mocked Title",
                "seo_filename": f"{seo_name}.jpg",
                "aspect_ratio": "4x5",
            }
            (processed_dir / f"{seo_name}-listing.json").write_text(
                json.dumps(listing), encoding="utf-8"
            )

            payload = {
                "success": True,
                "listing": listing,
                "sku": seo_name,
                "processed_folder": str(processed_dir),
            }
            stdout = json.dumps(payload)
            return _FakeCompletedProcess(
                returncode=0,
                stdout=(stdout if text else stdout.encode("utf-8")),
                stderr=("" if text else b""),
            )

        # Default noop result for other subprocess.run calls
        return _FakeCompletedProcess(
            returncode=0,
            stdout=("" if text else b""),
            stderr=("" if text else b""),
        )

    monkeypatch.setattr(subprocess, "run", _fake_run)

    # Ensure test environment allows session eviction
    monkeypatch.setattr(config, "ENVIRONMENT", "dev")
