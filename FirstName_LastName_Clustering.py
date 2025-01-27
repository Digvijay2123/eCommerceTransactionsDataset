import pandas as pd

from Notebook.FirstName_LastName_EDA import customers, transactions

customer_data = pd.merge(customers, transactions, on='CustomerID')


customer_features = customer_data.groupby('CustomerID').agg({
    'TotalValue': 'sum',
    'Quantity': 'sum',
    'TransactionDate': 'count'
}).reset_index()


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_features = scaler.fit_transform(customer_features[['TotalValue', 'Quantity', 'TransactionDate']])
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
customer_features['Cluster'] = kmeans.fit_predict(scaled_features)


from sklearn.metrics import davies_bouldin_score
db_index = davies_bouldin_score(scaled_features, customer_features['Cluster'])


sns.scatterplot(x=customer_features['TotalValue'], y=customer_features['Quantity'], hue=customer_features['Cluster'], palette='Set1')


customer_features.to_csv('Output/Clustering_Results.csv', index=False)
