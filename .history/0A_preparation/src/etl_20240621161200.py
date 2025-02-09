# full etl

import pandas as pd
import sqlite3

# Step 1: Extract
def extract_data(file_path):
    return pd.read_csv(file_path)

# Step 2: Transform
def transform_data(df):
    # Create a customers DataFrame
    customers = df[['customer_name', 'customer_email']].drop_duplicates().reset_index(drop=True)
    customers['customer_id'] = customers.index + 1
    
    # Create an orders DataFrame
    orders = df[['customer_email', 'order_id', 'order_date', 'order_amount']]
    orders = orders.merge(customers[['customer_email', 'customer_id']], on='customer_email', how='left')
    orders = orders.drop(columns=['customer_email'])
    
    return customers, orders

# Step 3: Load
def load_data(customers, orders, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Define the schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            customer_name TEXT NOT NULL,
            customer_email TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            order_date TEXT NOT NULL,
            order_amount REAL NOT NULL,
            customer_id INTEGER,
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
        )
    ''')
    
    # Load data into the database
    customers.to_sql('customers', conn, if_exists='replace', index=False)
    orders.to_sql('orders', conn, if_exists='replace', index=False)
    
    conn.commit()
    conn.close()

def main(file_path, db_path):
    df = extract_data(file_path)
    customers, orders = transform_data(df)
    load_data(customers, orders, db_path)

if __name__ == "__main__":
    file_path = 'data.csv'  # Path to your input CSV file
    db_path = 'database.db'  # Path to your SQLite database
    main(file_path, db_path)
