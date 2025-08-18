import json
from PIL import Image
from unittest import mock

# All necessary setup (app, config, client, login) is now handled by fixtures from conftest.py

def test_analyze_api_json_response(client, prevent_background_processes):
    """Tests that a successful analysis returns a valid JSON response."""
    # The 'client' fixture provides a logged-in client and a temporary filesystem.
    # The 'prevent_background_processes' fixture mocks the subprocess calls.
    
    # --- Setup ---
    # Create the test image inside the temporary directory provided by the client fixture
    unanalysed_root = client.application.config['UNANALYSED_ROOT']
    Image.new("RGB", (10, 10), "blue").save(unanalysed_root / "dummy.jpg")

    # This is the fake data our mocked analysis script will return
    dummy_entry = {
        "processed_folder": str(client.application.config['PROCESSED_ROOT'] / "dummy-artwork"),
        "listing": {"seo_filename": "dummy-artwork.jpg"},
        "aspect_ratio": "square",
    }

    # --- Action ---
    with mock.patch("routes.artwork_routes._run_ai_analysis", return_value=dummy_entry):
        response = client.post(
            "/analyze/square/dummy.jpg",
            headers={"X-Requested-With": "XMLHttpRequest"}
        )

    # --- Assert ---
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json().get("success") is True
    assert "redirect_url" in response.get_json()

def test_analyze_api_strips_binary_data(client, prevent_background_processes):
    """Tests that binary data (like image blobs) is stripped from the final JSON."""
    # --- Setup ---
    unanalysed_root = client.application.config['UNANALYSED_ROOT']
    Image.new("RGB", (10, 10), "green").save(unanalysed_root / "byte.jpg")

    dummy_entry = {
        "processed_folder": str(client.application.config['PROCESSED_ROOT'] / "byte-art"),
        "listing": {"seo_filename": "byte-art.jpg"},
        "blob": b"some_binary_data", # This should be stripped
    }

    # --- Action ---
    with mock.patch("routes.artwork_routes._run_ai_analysis", return_value=dummy_entry):
        response = client.post(
            "/analyze/square/byte.jpg",
            headers={"X-Requested-With": "XMLHttpRequest"}
        )

    # --- Assert ---
    assert response.status_code == 200
    assert "blob" not in response.get_data(as_text=True)

def test_analyze_api_handles_errors(client, prevent_background_processes):
    """Tests that the API returns a 500 error in a machine-readable format."""
    # --- Setup ---
    unanalysed_root = client.application.config['UNANALYSED_ROOT']
    Image.new("RGB", (10, 10), "red").save(unanalysed_root / "err.jpg")

    # --- Action ---
    with mock.patch("routes.artwork_routes._run_ai_analysis", side_effect=RuntimeError("A critical analysis error")):
        response = client.post(
            "/analyze/square/err.jpg",
            headers={"X-Requested-With": "XMLHttpRequest"}
        )

    # --- Assert ---
    assert response.status_code == 500
    assert response.is_json
    data = response.get_json()
    assert data.get("success") is False
    assert "A critical analysis error" in data.get("error")