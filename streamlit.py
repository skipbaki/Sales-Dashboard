import streamlit as st
import pandas as pd
import psycopg2
from config import DB_CONFIG
from queries import monthly_sales, top_products, top_customers, total_sales

st.set_page_config(page_title='Sales Dashboard', layout='wide')
st.title('Sales Dashboard - Sample Project')

# KPIs
ts = total_sales().iloc[0,0] if not total_sales().empty else 0
col1, col2, col3 = st.columns(3)
col1.metric('Total Sales', f"${ts:.2f}")
tp = top_products()
tc = top_customers()
col2.metric('Top Product', tp.iloc[0]['product'] if not tp.empty else 'N/A')
col3.metric('Top Customer', tc.iloc[0]['customer'] if not tc.empty else 'N/A')

st.markdown('### Monthly Sales Trend')
ms = monthly_sales()
if not ms.empty:
    st.line_chart(ms.set_index('month'))
else:
    st.write("No monthly sales data available.")

st.markdown('### Top Products by Revenue')
if not tp.empty:
    st.bar_chart(tp.set_index('product'))
else:
    st.write("No product data available.")

st.markdown('### Top Customers by Spending')
if not tc.empty:
    st.bar_chart(tc.set_index('customer'))
else:
    st.write("No customer data available.")

st.markdown('### Raw Data Samples')
try:
    conn = psycopg2.connect(**DB_CONFIG)
    customers_df = pd.read_sql_query('SELECT * FROM customers LIMIT 50', conn)
    st.dataframe(customers_df)
    conn.close()
except Exception as e:
    st.error(f"Error connecting to database: {e}")
