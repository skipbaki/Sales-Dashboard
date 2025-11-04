# Sales Dashboard (SQL + Python)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)  
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

## Project Overview

A sales analytics dashboard built with Python and PostgreSQL. This project features an interactive Streamlit web interface, automated data visualizations, and SQL queries to analyze sales performance, track top products and customers, and generate insightful business reports. I made this project specially for beginners to learn database management, data visualization, and full-stack analytics development with SQL + Python.

---

## Features

- Sales Analytics: Monthly sales trends, top products, and customer insights
- Data Export: Generate CSV reports and visual charts for further analysis
- PostgreSQL Integration: Robust database management with proper relationships
- Automated Reporting: Scripts to generate visualizations and export data

---

## Tech Stack

Backend: Python

Database: PostgreSQL

Visualization: Matplotlib

Data Processing: Pandas

Database Connection: Psycopg2

---

## Prerequisites
- PostgreSQL installed and running
- A database named 'sales_dashboard' created in PostgreSQL

---

## Installation & Setup

## Note:
Make sure your PostgreSQL server is running before executing the scripts.

1. **Clone this repository**
   ```bash
   git clone https://github.com/skipbaki/sales-dashboard.git
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
    DB_USER=postgres
    DB_PASSWORD=your_pass
    DB_PORT=5432

5. **Initialize Database**
   ```bash
   python products_db.py

---

## Generate Reports and Visualizations
1. **Export data to CSV files:**
   ```bash
   python queries.py
2. **Generate static visualizations:**
   ```bash
   python dashboard.py

---

## Customization

- Modify `schema.sql` to change the database structure
- Update `queries.py` to add new analytical queries
- Customize `dashboard.py` to create different visualizations

---

## Contributing

Feel free to submit issues and enhancement requests.

---
