import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customers = pd.read_csv('Data/Customers.csv')
products = pd.read_csv('Data/Products.csv')
transactions = pd.read_csv('Data/Transactions.csv')

# Data preprocess
customers['SignupDate'] = pd.to_datetime(customers['SignupDate'])
transactions['TransactionDate'] = pd.to_datetime(transactions['TransactionDate'])

# exploratory data analysis
sns.histplot(products['Price'], kde=True)
sns.barplot(x=region_distribution.index, y=region_distribution.values)

# buiss insight
# Example Insight
# print("Insight 1: Top-selling products contribute to X% of total sales.")
