import pytest
import shutil
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import subprocess

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config
from app import app as flask_app

# =============================================================================
# SECTION 1: PYTEST HOOKS
# =============================================================================

def pytest_addoption(parser):
    parser.addoption("--run-live-tests", action="store_true", default=False, help="run live API tests")

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
# SECTION 2: CORE FIXTURES
# =============================================================================

@pytest.fixture
def managed_artwork_paths(tmp_path_factory):
    """Creates a temporary, isolated directory structure for each test function."""
    base_dir = tmp_path_factory.mktemp("art_processing")
    paths = {
        "base": base_dir, # The root of our temporary world
        "unanalysed": base_dir / "unanalysed-artwork",
        "processed": base_dir / "processed-artwork",
    }
    for path in paths.values():
        if path.name != "base": # No need to create the base dir again
            path.mkdir(parents=True, exist_ok=True)
    yield SimpleNamespace(**paths)

@pytest.fixture
def client(managed_artwork_paths, monkeypatch):
    """
    The MASTER fixture. Provides a test client with a fully isolated and
    correctly patched filesystem configuration.
    """
    # --- THIS IS THE FINAL FIX ---
    # Patch ALL relevant filesystem config variables to point to our temp world.
    monkeypatch.setattr(config, 'BASE_DIR', managed_artwork_paths.base)
    monkeypatch.setattr(config, 'UNANALYSED_ROOT', managed_artwork_paths.unanalysed)
    monkeypatch.setattr(config, 'PROCESSED_ROOT', managed_artwork_paths.processed)
    
    flask_app.config["TESTING"] = True
    flask_app.config['BASE_DIR'] = managed_artwork_paths.base
    flask_app.config['UNANALYSED_ROOT'] = managed_artwork_paths.unanalysed
    flask_app.config['PROCESSED_ROOT'] = managed_artwork_paths.processed
    
    with flask_app.test_client() as test_client:
        test_client.post('/login', data={'username': 'robbie', 'password': 'kangaroo123'}, follow_redirects=True)
        yield test_client

@pytest.fixture
def prevent_background_processes(monkeypatch, managed_artwork_paths):
    """
    Prevents tests from launching real background subprocesses.
    """
    class _DummyPopen:
        def __init__(self, *args, **kwargs):
            self.args = args 
            self.returncode = 0
        def poll(self): return self.returncode
        def wait(self, timeout=None): return self.returncode
        def kill(self): pass

        def communicate(self, input=None, timeout=None):
            command_list = self.args[0]
            if len(command_list) > 1 and 'analyze_artwork.py' in command_list[1]:
                img_path = Path(command_list[2])
                seo_name = f"mocked-artwork-from-{img_path.stem}-by-test-RJC-MOCK"
                processed_dir = managed_artwork_paths.processed / seo_name
                processed_dir.mkdir(exist_ok=True)
                
                shutil.copy(img_path, processed_dir / f"{seo_name}.jpg")
                
                listing_data = {"title": "Mocked Title", "seo_filename": f"{seo_name}.jpg"}
                listing_file = processed_dir / f"{seo_name}-listing.json"
                listing_file.write_text(json.dumps(listing_data))

                payload = {
                    "success": True, "processed_folder": str(processed_dir),
                    "listing": listing_data, "sku": "RJC-MOCK-01"
                }
                return (json.dumps(payload).encode('utf-8'), b"")
            else:
                return (b"", b"")

        def __enter__(self): return self
        def __exit__(self, exc_type, exc, tb): return False

    monkeypatch.setattr(subprocess, "Popen", _DummyPopen)