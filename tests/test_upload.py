import io
from PIL import Image

def test_upload_single(client, managed_artwork_paths):
    """Tests a single successful file upload."""
    img_data = io.BytesIO()
    Image.new('RGB', (10, 10), 'red').save(img_data, format='JPEG')
    img_data.seek(0)

    resp = client.post(
        '/upload', 
        data={'images': (img_data, 'test.jpg')}, 
        content_type='multipart/form-data', 
        follow_redirects=True
    )
    
    assert resp.status_code == 200
    
    # Check that a new subfolder was created in our temp 'unanalysed' dir
    subfolders = [d for d in managed_artwork_paths.unanalysed.iterdir() if d.is_dir()]
    assert len(subfolders) == 1, "A new subfolder for the upload should have been created"
    
    # Check that the uploaded file exists inside that new folder
    created_files = list(subfolders[0].glob("*.jpg"))
    assert len(created_files) > 0, "The uploaded JPG should exist in the new subfolder"