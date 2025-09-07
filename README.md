Features
SQLite Database: Relational database with sample sales data

Data Analysis: Pre-built SQL queries for key sales metrics

Visualization: Static plots (Matplotlib) and interactive charts (Streamlit)

Export Functionality: Generate CSV reports and PNG visualizations

Web Dashboard: Interactive web interface built with Streamlit

Project Structure
text
sales-dashboard/
├── schema.sql           # Database schema and sample data
├── populate_db.py       # Database initialization script
├── queries.py           # SQL query functions and CSV export
├── dashboard.py         # Static visualization generation
├── streamlit_app.py     # Interactive web dashboard
├── requirements.txt     # Python dependencies
├── sales.db            # Generated SQLite database (after setup)
└── outputs/            # Generated reports and visualizations
    ├── *.csv           # Data exports
    ├── *.png           # Visualization images
    └── kpis.txt        # Key performance indicators
Setup Instructions
Clone the repository

bash
git clone <your-repo-url>
cd sales-dashboard
Install dependencies

bash
pip install -r requirements.txt
Initialize the database

bash
python populate_db.py
Generate reports and visualizations

bash
python queries.py      # Generates CSV files
python dashboard.py    # Generates PNG visualizations and KPI file
Launch the interactive dashboard

bash
streamlit run streamlit_app.py
Database Schema
The application uses a relational database with the following tables:

customers: Customer information

products: Product catalog

orders: Order records

order_items: Individual items within orders

payments: Payment transactions

Available Metrics
The dashboard provides insights into:

Total sales revenue

Monthly sales trends

Top products by revenue

Top customers by spending

Raw data exploration

Technologies Used
Python: Data processing and application logic

SQLite: Database management

Pandas: Data manipulation and analysis

Matplotlib: Static visualization

Streamlit: Interactive web dashboard

Usage
After setup, access the interactive dashboard by running streamlit run streamlit_app.py and navigating to the local URL provided (typically http://localhost:8501).

The application will display:

Key performance indicators at the top

Interactive charts for sales trends

Bar charts for top products and customers

Sample raw data from the database

Customization
You can modify the database schema in schema.sql or add new queries in queries.py to extend the functionality. The Streamlit dashboard in streamlit_app.py can be customized to display additional metrics or visualizations.
