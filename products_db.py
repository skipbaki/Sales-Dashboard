import os
from config import USE_SQLITE, DB_PATH, DB_CONFIG

schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")

if USE_SQLITE:
    import sqlite3
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
else:
    import psycopg2
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

with open(schema_path, "r") as f:
    sql = f.read()

# Execute SQL commands one by one
commands = sql.split(';')
for command in commands:
    if command.strip() != '':
        try:
            cur.execute(command)
        except Exception as e:
            print(f"Note: {e}")

conn.commit()
cur.close()
conn.close()

if USE_SQLITE:
    print("SQLite database created at:", DB_PATH)
else:
    print("PostgreSQL database populated successfully!")
