"""Download the YeaZ phase-contrast dataset (Dietler et al., 2020)."""

from pathlib import Path

import gdown

# Google Drive ID of the YeaZ phase-contrast training set.
# Source: https://www.epfl.ch/labs/lpbs/data-and-software/
FILE_ID = "14MUIN26ou0L12UC9UV_AC2S3isj1qBMY"

# Folder where the original (raw) data will be stored
raw_dir = Path("data") / "raw"
raw_dir.mkdir(parents=True, exist_ok=True)

archive_path = raw_dir / "gold-standard-PhC-plus-2.tar.gz"

print("Downloading YeaZ phase-contrast dataset...")
gdown.download(id=FILE_ID, output=str(archive_path), quiet=False)
print("Saved to", archive_path)