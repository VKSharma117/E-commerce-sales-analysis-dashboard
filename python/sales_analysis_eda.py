import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E-Commerce Project\Superstore csv file.csv")

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M')

df.info()
df.isnull().sum()
df.describe()

# Category-wise Sales & Profit
cat = df.groupby('Category')[['Sales','Profit']].sum().sort_values(by='Profit', ascending=False)
print(cat)

cat['Profit'].plot(kind='bar')
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.show()

# Sub-category
sub = df.groupby('Sub-Category')[['Sales','Profit']].sum().sort_values(by='Profit')
print(sub.head(10))   # worst
print(sub.tail(10))   # best

# Discount vs Profit
disc = df.groupby('Discount')['Profit'].mean()
print(disc)

plt.scatter(df['Discount'], df['Profit'])
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.show()

# Monthly Sales Trend
monthly = df.groupby('Month')['Sales'].sum()

monthly.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Top 10 Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_products)

top_products.plot(kind='bar')
plt.title("Top 10 Products by Sales")
plt.show()

# High Sales but Low Profit
prod = df.groupby('Product Name')[['Sales','Profit']].sum()

problem_products = prod[(prod['Sales'] > 10000) & (prod['Profit'] < 0)]
print(problem_products)

# Region Performance
region = df.groupby('Region')[['Sales','Profit']].sum()
print(region)

region['Profit'].plot(kind='bar')
plt.title("Profit by Region")
plt.show()

# Customer Segment Analysis
segment = df.groupby('Segment')[['Sales','Profit']].sum()
print(segment)

# Profit Margin
df['Profit Margin'] = df['Profit'] / df['Sales']

margin = df.groupby('Category')['Profit Margin'].mean()
print(margin)

print("End of code")

