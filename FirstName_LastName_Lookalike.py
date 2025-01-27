customer_transactions = pd.merge(transactions, customers, on='CustomerID')
customer_product_data = pd.merge(customer_transactions, products, on='ProductID')


customer_profile = customer_product_data.groupby(['CustomerID', 'ProductID']).agg({'Quantity': 'sum', 'Price': 'mean'}).reset_index()
customer_product_matrix = customer_profile.pivot_table(index='CustomerID', columns='ProductID', values='Quantity', fill_value=0)


from sklearn.metrics.pairwise import cosine_similarity
similarity_matrix = cosine_similarity(customer_product_matrix)


def get_similar_customers(customer_id, top_n=3):
    customer_idx = customer_product_matrix.index.get_loc(customer_id)
    similarity_scores = similarity_matrix[customer_idx]
    similar_customers = [(customer_product_matrix.index[i], similarity_scores[i]) for i in range(len(similarity_scores))]
    return sorted(similar_customers, key=lambda x: x[1], reverse=True)[:top_n]


lookalike_df.to_csv('Output/Lookalike.csv', index=False)
