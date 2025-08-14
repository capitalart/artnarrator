import subprocess
from pathlib import Path
import pytest

from routes.artwork_routes import _run_ai_analysis


def test_run_ai_analysis_timeout(monkeypatch):
    def fake_run(cmd, capture_output, text, timeout):
        raise subprocess.TimeoutExpired(cmd, timeout)
    monkeypatch.setattr(subprocess, 'run', fake_run)
    with pytest.raises(RuntimeError, match='timed out'):
        _run_ai_analysis(Path('img.jpg'), 'openai')


def test_run_ai_analysis_missing_script(monkeypatch):
    def fake_run(cmd, capture_output, text, timeout):
        raise FileNotFoundError('no such file')
    monkeypatch.setattr(subprocess, 'run', fake_run)
    with pytest.raises(RuntimeError, match='not found'):
        _run_ai_analysis(Path('img.jpg'), 'openai')
