# template for transforming data

# Step 2: Transform
def transform_data(df):
# handle each table. Best to do all tables here for their inter connection.


    # Create a customers DataFrame
    customers = df[['customer_name', 'customer_email']].drop_duplicates().reset_index(drop=True)
    customers['customer_id'] = customers.index + 1
    
    # Create an orders DataFrame
    orders = df[['customer_email', 'order_id', 'order_date', 'order_amount']]
    orders = orders.merge(customers[['customer_email', 'customer_id']], on='customer_email', how='left')
    orders = orders.drop(columns=['customer_email'])
    
    return customers, orders