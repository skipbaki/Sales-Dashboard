from config import USE_SQLITE, DB_CONFIG, DB_PATH

print("Testing database connection...")
print(f"Using SQLite: {USE_SQLITE}")

if USE_SQLITE:
    print(f"SQLite path: {DB_PATH}")
else:
    print("PostgreSQL config:", DB_CONFIG)
    
    # Test PostgreSQL connection
    try:
        import psycopg2
        conn = psycopg2.connect(**DB_CONFIG)
        print("PostgreSQL connection successful!")
        conn.close()
    except Exception as e:
        print(f"PostgreSQL connection failed: {e}")
        print("\n Set USE_SQLITE = True in config.py to use SQLite instead")
