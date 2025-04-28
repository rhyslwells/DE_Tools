import json
import sqlite3

# Load JSON data
with open('data.json', 'r') as f:
    data = json.load(f)

# Connect to SQLite (creates new file if it doesn't exist)
conn = sqlite3.connect('data.db')
cur = conn.cursor()

# Example: Assume JSON is a list of dictionaries
# [{"id":1, "name":"Alice"}, {"id":2, "name":"Bob"}]

# Create table
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT
)
''')

# Insert data
for item in data:
    cur.execute('INSERT INTO users (id, name) VALUES (?, ?)', (item['id'], item['name']))

conn.commit()
conn.close()
