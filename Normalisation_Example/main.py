import pandas as pd
import pyodbc

# Load the CSV file
df = pd.read_csv('file.csv')

# Split into incidents and locations
incidents = df[['Incident_Description', 'Location_Name']]
locations = df[['Location_Name']].drop_duplicates().reset_index(drop=True)

# Correct the database path to ensure it is properly formatted
db_path = r'C:\Users\RhysL\Desktop\normalisation_example\normal.accdb'  # Update this with the actual path to your database file

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

# Fetch the inserted locations with their IDs using pyodbc
cursor.execute('SELECT * FROM location')
location_records = cursor.fetchall()

# Convert the fetched data into a pandas DataFrame
location_ids = pd.DataFrame.from_records(location_records, columns=[col[0] for col in cursor.description])

# Map Location_Name to Location_ID
location_dict = location_ids.set_index('Location_Name')['Location_ID'].to_dict()
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
