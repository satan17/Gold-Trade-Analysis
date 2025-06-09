import os
from pathlib import Path

BASE_DIR = Path(os.getcwd())
DATASET_DIR = BASE_DIR / 'datasets'
DATASET_DIR.mkdir(exist_ok=True)