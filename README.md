# 📊 Sales Dashboard (SQL + Python + Streamlit)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)  
![SQLite](https://img.shields.io/badge/Database-SQLite-green.svg)  
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)  
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

## 🚀 Project Overview
This project demonstrates how to build a **Sales Analytics Dashboard** using:
- **SQLite** as the database (sample schema & data included)  
- **SQL** for querying KPIs (total sales, top products, monthly sales trends, etc.)  
- **Python (pandas & matplotlib)** for data analysis & visualization  
- **Streamlit** for an interactive web-based dashboard  

It’s designed as a beginner-friendly **end-to-end data project** that combines **SQL + Python** skills.  

---

## 📂 Project Structure



⚡ Features

✅ Create a sample sales database with customers, products, orders, and payments

✅ Run SQL queries to calculate KPIs:

Total sales

Monthly sales trend

Top 5 products by revenue

Top 5 customers by spending

✅ Visualize data with matplotlib

✅ Interactive dashboard with Streamlit

✅ Export results as CSV files & PNG charts

🛠️ Installation & Setup

Clone this repository

git clone https://github.com/yourusername/sales-dashboard.git
cd sales-dashboard


Install dependencies

pip install -r requirements.txt


Create the database (optional, sales.db is already included)

python populate_db.py


Generate KPI outputs

python queries.py
python dashboard.py


Run the Streamlit dashboard

streamlit run streamlit_app.py


🔮 Future Improvements

Add filters (by city, product category, date range)

Deploy dashboard online with Streamlit Cloud

Add user authentication for secure dashboards

Switch database to PostgreSQL/MySQL for larger datasets
