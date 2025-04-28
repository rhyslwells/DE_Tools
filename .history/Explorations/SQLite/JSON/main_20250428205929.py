import json
import pandas as pd
import sqlite3

# --- Load JSON ---
with open('example.json', 'r') as f:
    data = json.load(f)

# --- Normalize top-level ---
users_df = pd.json_normalize(data)

# --- Handle nested purchases separately ---
purchases_records = []
for user in data:
    user_id = user['user_id']
    for purchase in user.get('purchases', []):
        purchase['user_id'] = user_id
        purchases_records.append(purchase)

purchases_df = pd.DataFrame(purchases_records)

users_df = users_df.drop(columns=['purchases'])


# --- Fix users_df: stringify lists/dicts ---
# Before saving the DataFrame to SQLite, you need to convert any lists into strings (e.g., JSON strings) or drop/relocate them.

def safe_stringify(val):
    if isinstance(val, (list, dict)):
        return json.dumps(val)
    return val

for col in users_df.columns:
    users_df[col] = users_df[col].apply(safe_stringify)

# --- Write to SQLite ---
conn = sqlite3.connect('example.db')

users_df.to_sql('users', conn, if_exists='replace', index=False)
purchases_df.to_sql('purchases', conn, if_exists='replace', index=False)

conn.close()

# --- Read from SQLite ---
conn = sqlite3.connect('example.db')

users_df = pd.read_sql('SELECT * FROM users', conn)
purchases_df = pd.read_sql('SELECT * FROM purchases', conn)

conn.close()