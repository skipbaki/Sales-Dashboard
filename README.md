# 📊 Sales Dashboard (SQL + Python + Streamlit)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)  
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

## 🚀 Project Overview

A sales analytics dashboard built with Python and PostgreSQL. This project features an interactive Streamlit web interface, automated data visualizations, and robust SQL queries to analyze sales performance, track top products and customers, and generate insightful business reports. Perfect for learning database management, data visualization, and full-stack analytics development.

This project demonstrates how to build a Sales Analytics Dashboard using:
- **SQLite** as the database (sample schema & data included)  
- **SQL** for querying KPIs (total sales, top products, monthly sales trends, etc.)  
- **Python (pandas & matplotlib)** for data analysis & visualization  
- **Streamlit** for an interactive web-based dashboard  

**It’s designed as a beginner-friendly end-to-end data project that combines SQL + Python skills** 

---

## ⚡ Features

Interactive Dashboard: Real-time visualization of sales data through Streamlit

Sales Analytics: Monthly sales trends, top products, and customer insights

Data Export: Generate CSV reports and visual charts for further analysis

PostgreSQL Integration: Robust database management with proper relationships

Automated Reporting: Scripts to generate visualizations and export data

---

## 🛠️ Tech Stack

Backend: Python

Database: PostgreSQL

Visualization: Matplotlib, Streamlit

Data Processing: Pandas

Database Connection: Psycopg2

---

## Prerequisites
- PostgreSQL installed and running
- A database named 'sales_dashboard' created in PostgreSQL

---

## 🛠️ Installation & Setup

## Note:
Make sure your PostgreSQL server is running before executing the scripts.

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/sales-dashboard.git
   cd sales-dashboard
   
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set up PostgreSQL**
   ```bash
   Install PostgreSQL on your system

   Create a database named sales_dashboard

   Update the .env file with your database credentials:
    DB_HOST=localhost
    DB_NAME=sales_dashboard
    DB_USER=your_username
    DB_PASSWORD=your_password
    DB_PORT=1122

5. **Initialize Database**
   ```bash
   python populate_db.py

6. **Run the Streamlit dashboard**
   ```bash
   streamlit run streamlit.py

---

## Generate Reports and Visualizations
1. **Export data to CSV files:**
   ```bash
   python queries.py
2. **Generate static visualizations:**
   ```bash
   python dashboard.py

---

## 🔧 Customization

Modify schema.sql to change the database structure #edit the INSERT statements in schema.sql and rerun populate_db.py

Update queries.py to add new analytical queries

Customize dashboard.py to create different visualizations #modify the plotting code in dashboard.py or the chart configurations in streamlit.py

Extend streamlit_app.py to add new interactive elements

---

## 🔮 Future Improvements

- **User Authentication**: Add login system for multiple users with role-based access
- **Advanced Visualizations**: Integrate Plotly or D3.js for interactive charts
- **Predictive Analytics**: Implement machine learning for sales forecasting
- **Email Reports**: Automated scheduled report delivery via email
- **Mobile Responsive**: Optimize Streamlit dashboard for mobile devices
- **Data Import/Export**: Add functionality to import data from CSV/Excel files
- **Real-time Data**: Implement live data updates and websocket connections
- **Advanced Filtering**: Add date range filters and product/category filters
- **Docker Support**: Containerize the application for easier deployment
- **Cloud Deployment**: Prepare for deployment on AWS, Heroku, or DigitalOcean

---

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---
