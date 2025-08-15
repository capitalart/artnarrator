import pytest
import shutil
import json
from pathlib import Path

# Add project root to path to allow imports
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import config

def pytest_addoption(parser):
    parser.addoption(
        "--run-live-tests", action="store_true", default=False, help="run live API tests"
    )

def pytest_configure(config):
    config.addinivalue_line("markers", "live: marks tests as live")

def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-live-tests"):
        return
    skip_live = pytest.mark.skip(reason="need --run-live-tests option to run")
    for item in items:
        if "live" in item.keywords:
            item.add_marker(skip_live)

@pytest.fixture(scope="session", autouse=True)
def cleanup_tests(request):
    """A fixture to clean up all test-related files and folders after the entire test session is complete."""
    def final_cleanup():
        patterns = ["test-", "sample-", "good-", "bad-", "cassowary-test-01-test-run"]
        
        roots_to_clean = [
            Path(config.UNANALYSED_ROOT),
            Path(config.PROCESSED_ROOT)
        ]

        for root in roots_to_clean:
            if not root.exists():
                continue

            for item in root.iterdir():
                if item.is_dir() and any(p in item.name for p in patterns):
                    try:
                        shutil.rmtree(item)
                        print(f"✅ Cleaned up test folder: {item}")
                    except Exception as e:
                        print(f"⚠️ Could not delete test folder {item}: {e}")
        
        master_json_path = config.ART_PROCESSING_DIR / "master-artwork-paths.json"
        if master_json_path.exists():
            with open(master_json_path, "r+") as f:
                data = json.load(f)
                cleaned_data = {k: v for k, v in data.items() if not any(p in v.get("base", "") for p in patterns)}
                f.seek(0)
                json.dump(cleaned_data, f, indent=2)
                f.truncate()
            print("✅ Cleaned up test entries from master-artwork-paths.json")

    request.addfinalizer(final_cleanup)
