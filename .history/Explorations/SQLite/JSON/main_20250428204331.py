import json
import pandas as pd
import sqlite3

# --- Load JSON ---
with open('example.json', 'r') as f:
    data = json.load(f)

# --- Flatten JSON if necessary ---
# Normalize top-level
users_df = pd.json_normalize(data)

# Normalize nested 'purchases' with parent linkage
purchases_records = []
for user in data:
    user_id = user['user_id']
    for purchase in user.get('purchases', []):
        purchase['user_id'] = user_id  # add linkage
        purchases_records.append(purchase)

purchases_df = pd.DataFrame(purchases_records)

# --- Connect to SQLite ---
conn = sqlite3.connect('large_data.db')

# --- Store DataFrames to SQLite ---
users_df.to_sql('users', conn, if_exists='replace', index=False)
purchases_df.to_sql('purchases', conn, if_exists='replace', index=False)

conn.close()
