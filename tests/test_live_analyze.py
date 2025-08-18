import os
import json
import subprocess
from pathlib import Path

import pytest
from PIL import Image


@pytest.mark.skipif(os.environ.get('RUN_LIVE_ANALYZE') != '1',
                    reason='Live analyze tests are skipped by default. Set RUN_LIVE_ANALYZE=1 to enable')
def test_live_analyze_creates_processed_folder(tmp_path):
    """Run the real analysis CLI against a tiny generated image and assert end-to-end outputs.

    This test is intentionally skipped by default because it requires live API keys and
    modifies filesystem state under PROCESSED_ROOT. Enable by setting RUN_LIVE_ANALYZE=1.
    """
    # create a tiny image
    img_path = tmp_path / "live-test.jpg"
    Image.new('RGB', (40, 40), 'white').save(img_path)

    # run the analysis CLI with --json-output
    cli = Path.cwd() / 'scripts' / 'analyze_artwork.py'
    proc = subprocess.run(["python3", str(cli), str(img_path), "--json-output"], capture_output=True, text=True)
    assert proc.returncode == 0, f"analyze CLI failed: {proc.stderr}\nstdout: {proc.stdout[:1000]}"

    data = json.loads(proc.stdout)
    assert 'processed_folder' in data, 'processed_folder missing from CLI JSON output'
    processed_folder = Path(data['processed_folder'])
    assert processed_folder.exists(), f'processed_folder does not exist: {processed_folder}'

    # listing JSON should be created inside the processed folder
    listing_file = processed_folder / (processed_folder.name + '-listing.json')
    assert listing_file.exists(), f'listing JSON not found: {listing_file}'
    listing = json.loads(listing_file.read_text())

    # Basic expected fields
    assert ('seo_filename' in listing) or ('filename' in listing), 'seo/filename missing in listing'
    assert 'aspect_ratio' in listing, 'aspect_ratio missing in listing'
