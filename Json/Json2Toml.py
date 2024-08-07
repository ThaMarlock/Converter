import json
import toml
import os

def convert_json_to_toml(input_path):
    # Check if the file exists
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"The file {input_path} does not exist.")
    
    # Read the JSON data from the file
    with open(input_path, 'r') as json_file:
        json_data = json.load(json_file)
    
    # Determine the output file path
    output_path = os.path.splitext(input_path)[0] + '.toml'
    
    # Write the TOML data to the output file
    with open(output_path, 'w') as toml_file:
        toml.dump(json_data, toml_file)
    
    print(f"Converted {input_path} to {output_path}")

if __name__ == "__main__":
    # Prompt the user for the JSON file path
    input_file = input("Enter the path to the JSON file: ")
    try:
        convert_json_to_toml(input_file)
    except Exception as e:
        print(f"An error occurred: {e}")
