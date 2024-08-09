import xmltodict
import json
import os

def convert_xml_to_json():
    # Ask the user for the input XML file path
    xml_file_path = input("Enter the path to the XML file: ").strip()

    # Check if the file exists
    if not os.path.isfile(xml_file_path):
        print("The specified file does not exist. Please check the path and try again.")
        return

    # Determine the JSON file path
    json_file_path = os.path.splitext(xml_file_path)[0] + '.json'

    # Read the XML file
    with open(xml_file_path, 'r') as xml_file:
        xml_content = xml_file.read()

    # Parse XML content and convert to a dictionary
    dict_data = xmltodict.parse(xml_content)

    # Convert dictionary to JSON
    json_data = json.dumps(dict_data, indent=4)

    # Write JSON data to file
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_data)

    print(f'XML has been converted to JSON and saved to {json_file_path}')

if __name__ == "__main__":
    convert_xml_to_json()
