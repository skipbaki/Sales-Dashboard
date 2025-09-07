import sqlite3, os
BASE_DIR = os.path.dirname(__file__)
db_path = os.path.join(BASE_DIR, "sales.db")
schema_path = os.path.join(BASE_DIR, "schema.sql")

if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)
cur = conn.cursor()
with open(schema_path, "r") as f:
    sql = f.read()
cur.executescript(sql)
conn.commit()
conn.close()
print("Database created at:", db_path)
