import pytest
import os
import sys
from pathlib import Path

# Add project root to path to allow imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# This will skip the test unless you run pytest with '--run-live-tests'
LIVE_TESTS = pytest.mark.skipif(
    "not config.getoption('--run-live-tests')",
    reason="needs --run-live-tests option to run"
)

@pytest.fixture(scope="module")
def connection_tester():
    """Imports the connection tester script."""
    from scripts import test_connections
    return test_connections

@LIVE_TESTS
def test_openai_connection(connection_tester):
    """Tests the OpenAI API connection."""
    try:
        connection_tester.test_openai()
    except Exception as e:
        pytest.fail(f"OpenAI connection test failed: {e}")

@LIVE_TESTS
def test_google_gemini_connection(connection_tester):
    """Tests the Google Gemini API connection."""
    try:
        connection_tester.test_google_gemini()
    except Exception as e:
        pytest.fail(f"Google Gemini connection test failed: {e}")

@LIVE_TESTS
def test_sellbrite_connection(connection_tester):
    """Tests the Sellbrite API connection."""
    try:
        connection_tester.test_sellbrite()
    except Exception as e:
        pytest.fail(f"Sellbrite connection test failed: {e}")