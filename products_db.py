import os
import sqlite3
from config import USE_SQLITE, DB_PATH, DB_CONFIG

schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")

if USE_SQLITE:
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # Enable foreign key support in SQLite
    cur.execute("PRAGMA foreign_keys = ON;")
    
    # Read and modify schema for SQLite
    with open(schema_path, "r") as f:
        sql = f.read()
    
    # Replace SERIAL with INTEGER PRIMARY KEY AUTOINCREMENT (only once per line)
    lines = sql.split('\n')
    modified_lines = []
    
    for line in lines:
        if 'SERIAL PRIMARY KEY' in line:
            # Replace SERIAL PRIMARY KEY with INTEGER PRIMARY KEY AUTOINCREMENT
            line = line.replace('SERIAL PRIMARY KEY', 'INTEGER PRIMARY KEY AUTOINCREMENT')
        elif 'SERIAL' in line and 'PRIMARY KEY' in line:
            line = line.replace('SERIAL', 'INTEGER PRIMARY KEY AUTOINCREMENT')
        modified_lines.append(line)
    
    sql = '\n'.join(modified_lines)
    
    # Execute each CREATE TABLE statement separately
    import re
    
    # Find all CREATE TABLE statements
    create_statements = re.findall(r'CREATE TABLE.*?;', sql, re.DOTALL | re.IGNORECASE)
    
    # First create all tables
    for statement in create_statements:
        try:
            cur.execute(statement)
            print(f"✓ Created table: {statement.split()[2]}")
        except Exception as e:
            print(f"✗ Error creating table: {e}")
    
    # Then execute INSERT statements
    insert_statements = re.findall(r'INSERT INTO.*?;', sql, re.DOTALL | re.IGNORECASE)
    
    for statement in insert_statements:
        try:
            cur.execute(statement)
        except Exception as e:
            print(f"✗ Error inserting data: {e}")
    
    conn.commit()
    
    # Verify tables
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    print("\n✓ Tables created:")
    for table in tables:
        print(f"  - {table[0]}")
    
    # Count records
    for table in tables:
        cur.execute(f"SELECT COUNT(*) FROM {table[0]}")
        count = cur.fetchone()[0]
        print(f"  {table[0]}: {count} records")
    
    cur.close()
    conn.close()
    
    print(f"\n✓ SQLite database created at: {DB_PATH}")

else:
    # PostgreSQL version
    import psycopg2
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    with open(schema_path, "r") as f:
        sql = f.read()
    
    commands = sql.split(';')
    for command in commands:
        if command.strip():
            try:
                cur.execute(command)
            except Exception as e:
                print(f"Note: {e}")
    
    conn.commit()
    cur.close()
    conn.close()
    print("PostgreSQL database populated successfully!")
