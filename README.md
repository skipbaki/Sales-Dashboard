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

├── schema.sql              # Database schema and sample data
├── populate_db.py          # Database initialization script
├── sales.db                # Generated SQLite database (after running populate_db.py)
├── queries.py              # Data query functions and CSV export
├── dashboard.py            # Static visualization generation
├── streamlit_app.py        # Interactive web dashboard
├── requirements.txt        # Python dependencies
└── outputs/                # Generated outputs (CSVs, plots, KPIs)
    ├── monthly_sales.csv
    ├── top_products.csv
    ├── top_customers.csv
    ├── total_sales.csv
    ├── monthly_sales.png
    ├── top_products.png
    ├── top_customers.png
    └── kpis.txt


---

## ⚡ Features
- ✅ Create a sample sales database with customers, products, orders, and payments  
- ✅ Run SQL queries to calculate **KPIs**:  
  - Total sales  
  - Monthly sales trend  
  - Top 5 products by revenue  
  - Top 5 customers by spending  
- ✅ Visualize data with **matplotlib**  
- ✅ Interactive dashboard with **Streamlit**  
- ✅ Export results as **CSV files & PNG charts**  

---

## 🛠️ Installation & Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/sales-dashboard.git
   cd sales-dashboard
   
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Database Setup**
   ```bash
   python populate_db.py

## Generate Reports and Visualizations
1. **Export data to CSV files:**
   ```bash
   python queries.py
2. **Generate static visualizations:**
   ```bash
   python dashboard.py

## Launch Interactive Dashboard
**Start the Streamlit web application:**

bash
streamlit run streamlit_app.py
The dashboard will open in your default web browser at http://localhost:8501. 
