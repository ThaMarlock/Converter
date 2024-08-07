import json
import yaml
import os

def convert_json_to_yaml(input_path):
    # Check if the file exists
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"The file {input_path} does not exist.")
    
    # Read the JSON data from the file
    with open(input_path, 'r') as json_file:
        json_data = json.load(json_file)
    
    # Determine the output file path
    output_path = os.path.splitext(input_path)[0] + '.yaml'
    
    # Write the YAML data to the output file
    with open(output_path, 'w') as yaml_file:
        yaml.dump(json_data, yaml_file, default_flow_style=False)
    
    print(f"Converted {input_path} to {output_path}")

if __name__ == "__main__":
    # Example usage: Replace 'input.json' with the path to your JSON file
    input_file = 'input.json'
    convert_json_to_yaml(input_file)
