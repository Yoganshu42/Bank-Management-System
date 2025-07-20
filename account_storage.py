import json
import os
customer_data = {}

def store_details(new_data):
    file_path = r'C:\Users\yogan\OneDrive\Desktop\python_practice\Bank Management\customer_data.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = {}
    else:
        existing_data = {}

    existing_data.update(new_data)
    
    with open(file_path, 'w') as f:
        json.dump(existing_data, f, indent = 4)
        print("\n\t\t\tDATA SAVED SUCCESSFULLY")


def load_json():
    file_path = r'C:\Users\yogan\OneDrive\Desktop\python_practice\Bank Management\customer_data.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return{}
    return{}