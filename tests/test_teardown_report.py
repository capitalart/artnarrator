import json, uuid
from pathlib import Path
from tests._session_cleaner import session_cleaner_context

def test_session_cleaner_context_restores_and_removes():
    repo_root = Path(__file__).resolve().parent.parent
    art_proc = repo_root / "art-processing"
    processed = art_proc / "processed-artwork"
    master = art_proc / "master-artwork-paths.json"

    uniq = uuid.uuid4().hex[:8]

    with session_cleaner_context():
        processed.mkdir(parents=True, exist_ok=True)
        test_folder = processed / f"pytest-temp-to-remove-{uniq}"
        test_folder.mkdir(parents=True, exist_ok=True)
        (test_folder / "dummy.txt").write_text("hello", encoding="utf-8")

        art_proc.mkdir(parents=True, exist_ok=True)
        if master.exists():
            try:
                data = json.loads(master.read_text(encoding="utf-8"))
                if isinstance(data, dict):
                    data[f"__pytest_test_marker__{uniq}"] = "created"
                else:
                    data = {f"__pytest_test_marker__{uniq}": "created"}
            except Exception:
                data = {f"__pytest_test_marker__{uniq}": "created"}
        else:
            data = {f"__pytest_test_marker__{uniq}": "created"}
        master.write_text(json.dumps(data, indent=2), encoding="utf-8")

    assert not test_folder.exists(), f"Residual test folder still exists: {test_folder}"
    if master.exists():
        data = json.loads(master.read_text(encoding="utf-8"))
        assert f"__pytest_test_marker__{uniq}" not in data, "Master JSON still contains test marker"
