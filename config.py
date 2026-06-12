from pathlib import Path

ANALYSIS_DIR = Path(__file__).resolve().parent
DATA_DIR     = ANALYSIS_DIR / "data"
RAW_DIR      = DATA_DIR / "raw"
OUTPUT_DIR   = ANALYSIS_DIR / "output"

for _dir in [DATA_DIR, RAW_DIR, OUTPUT_DIR]:
    _dir.mkdir(parents=True, exist_ok=True)
