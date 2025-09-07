import os
import pandas as pd
import psycopg2
from config import DB_CONFIG

def run_query(sql):
    conn = psycopg2.connect(**DB_CONFIG)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df

def total_sales():
    sql = "SELECT SUM(amount) AS total_sales FROM payments;"
    return run_query(sql)

def monthly_sales():
    sql = """
SELECT TO_CHAR(TO_DATE(order_date, 'YYYY-MM-DD'), 'YYYY-MM') AS month, 
       SUM(oi.quantity * oi.unit_price) AS monthly_sales
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY TO_CHAR(TO_DATE(order_date, 'YYYY-MM-DD'), 'YYYY-MM')
ORDER BY month;
"""
    return run_query(sql)

def top_products(limit=5):
    sql = f"""
SELECT p.name AS product, SUM(oi.quantity * oi.unit_price) AS revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.name
ORDER BY revenue DESC
LIMIT {limit};
"""
    return run_query(sql)

def top_customers(limit=5):
    sql = f"""
SELECT c.name AS customer, SUM(oi.quantity * oi.unit_price) AS spending
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.name
ORDER BY spending DESC
LIMIT {limit};
"""
    return run_query(sql)

if __name__ == '__main__':
    os.makedirs(os.path.join(os.path.dirname(__file__), "outputs"), exist_ok=True)
    total_sales().to_csv(os.path.join(os.path.dirname(__file__), "outputs", "total_sales.csv"), index=False)
    monthly_sales().to_csv(os.path.join(os.path.dirname(__file__), "outputs", "monthly_sales.csv"), index=False)
    top_products().to_csv(os.path.join(os.path.dirname(__file__), "outputs", "top_products.csv"), index=False)
    top_customers().to_csv(os.path.join(os.path.dirname(__file__), "outputs", "top_customers.csv"), index=False)
    print("KPI CSVs saved to outputs/")
