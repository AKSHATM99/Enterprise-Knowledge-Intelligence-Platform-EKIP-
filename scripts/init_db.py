from services.db import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    created_at TEXT
)
""")

cur.executemany(
    "INSERT INTO users (name, created_at) VALUES (?, ?)",
    [
        ("Alice", "2024-01-01"),
        ("Bob", "2024-01-02"),
        ("Charlie", "2024-01-02")
    ]
)

conn.commit()
conn.close()

print("Database initialized")
