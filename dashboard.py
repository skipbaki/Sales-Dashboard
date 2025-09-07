import os, pandas as pd, matplotlib.pyplot as plt
BASE_DIR = os.path.dirname(__file__)
outputs = os.path.join(BASE_DIR, "outputs")
os.makedirs(outputs, exist_ok=True)

from queries import monthly_sales, top_products, top_customers, total_sales

# Monthly sales plot
ms = monthly_sales()
plt.figure(figsize=(8,5))
plt.plot(ms['month'], ms['monthly_sales'], marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(outputs, 'monthly_sales.png'))
plt.close()

# Top products bar chart
tp = top_products()
plt.figure(figsize=(8,5))
plt.bar(tp['product'], tp['revenue'])
plt.title('Top Products by Revenue')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig(os.path.join(outputs, 'top_products.png'))
plt.close()

# Top customers bar chart
tc = top_customers()
plt.figure(figsize=(8,5))
plt.bar(tc['customer'], tc['spending'])
plt.title('Top Customers by Spending')
plt.xlabel('Customer')
plt.ylabel('Spending')
plt.tight_layout()
plt.savefig(os.path.join(outputs, 'top_customers.png'))
plt.close()

# Save aggregated KPIs as text
ts = total_sales().iloc[0,0]
with open(os.path.join(outputs, 'kpis.txt'), 'w') as f:
    f.write(f"Total Sales: {ts}\n")
print('Plots and KPIs generated in outputs/')
