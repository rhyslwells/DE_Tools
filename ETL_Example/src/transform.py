# template for transforming data



"""#     Foreign Key Relationships:

#     Identify and establish foreign key relationships between tables.
#     Ensure referential integrity by matching foreign keys with primary keys.
#     Data Normalization:

#     Split data into multiple tables to reduce redundancy.
#     Ensure that each table contains only related data (e.g., separate customers and orders).
"""


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


import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='logs/etl.log', filemode='w')

def clean_data(df):
    # General data cleaning logic (can be extended)
    df = df.dropna()  # Example: drop rows with any missing values
    return df

def normalize_column_names(df):
    # Normalize column names to lower case with underscores
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    return df

def prepare_dataframes(df_dict, relationships):
    """
    Generalized transformation function to prepare DataFrames for a relational database.

    :param df_dict: Dictionary of DataFrames with table names as keys.
    :param relationships: Dictionary defining foreign key relationships.
    :return: Transformed dictionary of DataFrames.
    """
    transformed_dfs = {}
    
    for table_name, df in df_dict.items():
        try:
            logging.info(f"Transforming table: {table_name}")

            # Clean and normalize data
            df = clean_data(df)
            df = normalize_column_names(df)

            # Apply table-specific transformations
            if table_name in relationships:
                for fk, ref_table in relationships[table_name].items():
                    if ref_table in transformed_dfs:
                        df = df.merge(transformed_dfs[ref_table][[fk]], on=fk, how='left')

            # Additional custom transformations
            if table_name == 'orders':
                df['order_date'] = pd.to_datetime(df['order_date'])
            elif table_name == 'customers':
                df['customer_name'] = df['customer_name'].str.title()

            transformed_dfs[table_name] = df
            logging.info(f"Transformation successful for table: {table_name}")

        except Exception as e:
            logging.error(f"Error transforming table {table_name}: {e}")
            continue

    return transformed_dfs

def main():
    # Example data
    data_files = {
        'customers': 'data/customers.csv',
        'orders': 'data/orders.csv'
    }
    
    df_dict = {table: pd.read_csv(path) for table, path in data_files.items()}
    
    # Define relationships
    relationships = {
        'orders': {'customer_email': 'customers'}
    }
    
    transformed_dfs = prepare_dataframes(df_dict, relationships)
    
    # Proceed with loading the transformed data into the database
    # ...

if __name__ == "__main__":
    main()
