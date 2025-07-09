import os
import pandas as pd
from datetime import datetime

def create_folder_structure():
    # Create timestamp for folder name
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    base_folder = f'Handback-Example-Structure-{timestamp}'
    
    # Create the base folder
    os.makedirs(base_folder, exist_ok=True)
    
    # Read the CSV file
    df = pd.read_csv('Data Catalog - Handback Mapping.csv')

    # Convert DataFrame to dictionary
    folders = dict(zip(df['Folder_ID'].astype(str), df['Folder_Name']))

    # Function to build full path
    def get_full_path(folder_id):
        path_parts = []
        current_id = folder_id
        
        while current_id:
            path_parts.insert(0, folders[current_id])
            # If it's a root folder (no dots), break
            if '.' not in current_id:
                break
            # Get parent ID by removing the last part
            current_id = '.'.join(current_id.split('.')[:-1])
            
        return os.path.join(base_folder, *path_parts)

    # Create all folders
    for folder_id, folder_name in folders.items():
        full_path = get_full_path(folder_id)
        os.makedirs(full_path, exist_ok=True)

if __name__ == '__main__':
    create_folder_structure()