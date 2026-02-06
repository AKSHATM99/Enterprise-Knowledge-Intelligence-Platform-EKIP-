import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]   # ekip/
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "app.db"

def get_connection():
    DATA_DIR.mkdir(parents=True, exist_ok=True)  # 👈 critical
    return sqlite3.connect(DB_PATH)
