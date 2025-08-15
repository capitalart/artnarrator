# tests/test_analyze_artwork.py
# ======================================================================================
# FILE: tests/test_analyze_artwork.py
# DESCRIPTION: Test /analyze API endpoint and ensure proper HTML response.
# AUTHOR: Robbie Mode™ Patch - 2025-08-15 (Final Cleaned Version)
# ======================================================================================

import os
import shutil
import pytest
from pathlib import Path
from PIL import Image
import sys
import json

# Add project root to path before other imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app
import config
from dotenv import load_dotenv

# Load environment variables from system .env
load_dotenv(dotenv_path="/home/art/.env", override=True)

# ======================================================================================
# SECTION 1: Setup
# ======================================================================================

@pytest.fixture
def client():
    """Flask test client fixture for HTTP request simulation."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        # Log in a test user for the session
        with client.session_transaction() as sess:
            sess['logged_in'] = True
            sess['username'] = 'testuser'
        yield client

# ======================================================================================
# SECTION 2: Test Analyze Route – HTML Response
# ======================================================================================

def test_analyze_api_html_response(client):
    """
    Ensure that /analyze/<aspect>/<filename> returns valid HTML content after redirect.
    """
    # --- [ 2.0: Skip if dummy API key ] ---
    openai_key = os.getenv("OPENAI_API_KEY", "test")
    if openai_key.strip().lower() == "test" or not openai_key:
        pytest.skip("Skipping test: Requires a valid OPENAI_API_KEY")

    # --- [ 2.1: Prepare test image and folder structure ] ---
    base_filename = "cassowary-test-01"
    unique_id = "test-run"
    filename = f"{base_filename}-{unique_id}.jpg"
    aspect = "4x5"
    
    unanalysed_subfolder = config.UNANALYSED_ROOT / f"{base_filename}-{unique_id}"
    unanalysed_subfolder.mkdir(parents=True, exist_ok=True)
    destination_img_path = unanalysed_subfolder / filename

    # Create a dummy image file from scratch
    try:
        Image.new("RGB", (100, 125), "blue").save(destination_img_path)
    except Exception as e:
        pytest.fail(f"Failed to create dummy test image: {e}")

    # --- [ 2.2: POST to the /analyze route and follow redirect ] ---
    response = client.post(f"/analyze/{aspect}/{filename}", data={'provider': 'openai'}, follow_redirects=True)

    # --- [ 2.3: Validate response is HTML and contains hidden marker for Edit Page ] ---
    assert response.status_code == 200, "❌ Expected HTTP 200 OK from /analyze redirect"
    assert b"<html" in response.data or b"<div" in response.data, "❌ Expected HTML structure"
    assert b'id="edit-listing-marker"' in response.data, "❌ Edit page marker not found in HTML"