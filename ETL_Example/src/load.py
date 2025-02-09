# uses schema.sql 

def load_data(customers, orders, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    

    #####################################################
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
    #####################################################

    # Load data into the database
    customers.to_sql('customers', conn, if_exists='replace', index=False)
    orders.to_sql('orders', conn, if_exists='replace', index=False)
    
    conn.commit()
    conn.close()