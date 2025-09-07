import os
from dotenv import load_dotenv

load_dotenv()

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'sales_dashboard'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'postgres'),
    'port': os.getenv('DB_PORT', '5432')
}

# For quick testing - set to True if PostgreSQL isn't working
USE_SQLITE = True

if USE_SQLITE:
    BASE_DIR = os.path.dirname(__file__)
    DB_PATH = os.path.join(BASE_DIR, "sales.db")
