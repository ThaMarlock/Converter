import json
import csv
import os

def json_to_csv(json_file_path):
    # Read the JSON data
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Check if the JSON data is a list of dictionaries
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON data should be a list of dictionaries")

    # Determine the CSV file path
    csv_file_path = os.path.splitext(json_file_path)[0] + '.csv'

    # Get the headers from the keys of the first dictionary
    headers = data[0].keys()

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
