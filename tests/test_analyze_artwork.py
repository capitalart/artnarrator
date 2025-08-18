from PIL import Image
import os
import pytest

@pytest.mark.skipif(not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY") == "test", reason="Requires a valid OPENAI_API_KEY")
def test_analyze_redirects_successfully_on_mocked_success(client, prevent_background_processes):
    """
    Tests that the /analyze route correctly redirects to the edit page
    after a mocked, successful analysis.
    """
    # --- Setup ---
    filename = "cassowary-test-01.jpg"
    unanalysed_root = client.application.config['UNANALYSED_ROOT']
    
    unanalysed_subfolder = unanalysed_root / "cassowary-test-01"
    unanalysed_subfolder.mkdir(parents=True, exist_ok=True)
    destination_img_path = unanalysed_subfolder / filename
    Image.new("RGB", (100, 125), "blue").save(destination_img_path)

    # --- Action ---
    response = client.post(
        f"/analyze/4x5/{filename}", 
        data={'provider': 'openai'}, 
        follow_redirects=True
    )

    # --- Assert ---
    # Check that the final URL path after all redirects is the correct edit page URL.
    # This is more robust than checking for a specific piece of HTML.
    assert response.status_code == 200
    
    expected_seo_filename = "mocked-artwork-from-cassowary-test-01-by-test-RJC-MOCK.jpg"
    expected_final_path = f"/edit-listing/4x5/{expected_seo_filename}"
    
    assert response.request.path == expected_final_path, f"Expected to be on {expected_final_path} but was on {response.request.path}"