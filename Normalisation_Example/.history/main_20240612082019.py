import pandas as pd
import pyodbc

# Load the CSV file
df = pd.read_csv('file.csv')

# Split into incidents and locations
incidents = df[['Incident_Description', 'Location_Name']]
locations = df[['Location_Name']].drop_duplicates().reset_index(drop=True)

# Correct the database path to ensure it is properly formatted
db_path = r'C:\normal.accdb'  # Update this with the actual path to your database file

# Connection string to the Access database
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    rf'DBQ={db_path};'
)

# Connect to the Access database
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Insert unique locations into the location table
for index, row in locations.iterrows():
    cursor.execute("INSERT INTO location (Location_Name) VALUES (?)", row['Location_Name'])
conn.commit()

# Fetch the inserted locations with their IDs
location_ids = pd.read_sql('SELECT * FROM location', conn)
location_dict = location_ids.set_index('Location_Name')['Location_ID'].to_dict()

# Map Location_Name to Location_ID
incidents['Location_ID'] = incidents['Location_Name'].map(location_dict)

# Drop the Location_Name column as it's no longer needed
incidents = incidents.drop(columns=['Location_Name'])

# Insert incidents into the incidents table
for index, row in incidents.iterrows():
    cursor.execute("INSERT INTO incidents (Incident_Description, Location_ID) VALUES (?, ?)",
                   row['Incident_Description'], row['Location_ID'])
conn.commit()

# Close the connection
conn.close()
