import os
import psycopg2
from config import DB_CONFIG

schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")

# Connect to PostgreSQL
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

# Read and execute schema.sql
with open(schema_path, "r") as f:
    sql = f.read()

# Execute SQL commands one by one
commands = sql.split(';')
for command in commands:
    if command.strip() != '':
        try:
            cur.execute(command)
        except Exception as e:
            print(f"Error executing command: {command}")
            print(f"Error: {e}")

conn.commit()
cur.close()
conn.close()
print("Database schema created and populated successfully.")
