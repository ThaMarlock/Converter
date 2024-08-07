import json
import csv
import os

def json_to_csv(json_file_path):
    # Read the JSON data
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Determine if data is a list of dictionaries
    if isinstance(data, list):
        # If the list is not empty and contains dictionaries
        if data and isinstance(data[0], dict):
            headers = data[0].keys()
        else:
            raise ValueError("The JSON list is empty or does not contain dictionaries.")
    elif isinstance(data, dict):
        # Handle the case where the JSON data is a single dictionary
        headers = data.keys()
        data = [data]  # Convert to list of one dictionary
    else:
        raise ValueError("JSON data should be either a list of dictionaries or a single dictionary.")

    # Determine the CSV file path
    csv_file_path = os.path.splitext(json_file_path)[0] + '.csv'

    # Write the CSV data
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"CSV file has been created at: {csv_file_path}")

if __name__ == "__main__":
    # Ask the user for the JSON file path
    json_file_path = input("Enter the path to the JSON file: ")
    
    if not os.path.isfile(json_file_path):
        print(f"File not found: {json_file_path}")
    else:
        try:
            json_to_csv(json_file_path)
        except Exception as e:
            print(f"An error occurred: {e}")
