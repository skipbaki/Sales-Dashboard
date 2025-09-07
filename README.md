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

---

## 📈 Features
Total Sales Overview: Key metric showing overall sales performance

Monthly Sales Trends: Line chart visualizing sales over time

Product Performance: Bar chart showing top products by revenue

Customer Analysis: Bar chart showing top customers by spending

Raw Data Access: Sample view of the underlying customer data

---

## 🗃️ Database Schema
The SQLite database contains the following tables:

customers: Customer information (name, city, email)

products: Product details (name, category, price)

orders: Order records with timestamps

order_items: Individual items within orders

payments: Payment information for orders

---

## 🔧 Customization
To modify the sample data, edit the INSERT statements in schema.sql and rerun populate_db.py.

To change visualizations, modify the plotting code in dashboard.py or the chart configurations in streamlit_app.py

---

## 📋 Dependencies
pandas: Data manipulation and analysis

matplotlib: Static visualizations

streamlit: Interactive web dashboard

sqlite3: Database operations (included in Python standard library)

---

## 🔮 Future Improvements

Add filters (by city, product category, date range)

Deploy dashboard online with Streamlit Cloud

Add user authentication for secure dashboards

Switch database to PostgreSQL/MySQL for larger datasets

---

## 🤝 Contributing
Feel free to submit issues and enhancement requests!

---

## 📄 License
This project is open source and available under the MIT License.
