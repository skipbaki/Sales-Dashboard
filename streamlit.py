# streamlit_app.py - run with: streamlit run streamlit_app.py
import streamlit as st
import pandas as pd, os, sqlite3
from queries import monthly_sales, top_products, top_customers, total_sales

st.set_page_config(page_title='Sales Dashboard', layout='wide')
st.title('Sales Dashboard - Sample Project')

# KPIs
ts = total_sales().iloc[0,0] if not total_sales().empty else 0
col1, col2, col3 = st.columns(3)
col1.metric('Total Sales', f"{ts:.2f}")
tp = top_products()
tc = top_customers()
col2.metric('Top Product', tp.iloc[0]['product'] if not tp.empty else 'N/A')
col3.metric('Top Customer', tc.iloc[0]['customer'] if not tc.empty else 'N/A')

st.markdown('### Monthly Sales Trend')
st.line_chart(monthly_sales().set_index('month'))

st.markdown('### Top Products by Revenue')
st.bar_chart(top_products().set_index('product'))

st.markdown('### Top Customers by Spending')
st.bar_chart(top_customers().set_index('customer'))

st.markdown('### Raw Data Samples')
conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'sales.db'))
st.dataframe(pd.read_sql_query('SELECT * FROM customers LIMIT 50', conn))
conn.close()
