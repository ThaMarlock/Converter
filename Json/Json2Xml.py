import json
import xml.etree.ElementTree as ET
import os
from xml.dom import minidom

def json_to_xml(json_obj, root_tag='root'):
    def dict_to_xml(tag, d):
        elem = ET.Element(tag)
        for key, val in d.items():
            if isinstance(val, dict):
                child = dict_to_xml(key, val)
                elem.append(child)
            elif isinstance(val, list):
                for i, item in enumerate(val):
                    child = dict_to_xml(f"{key}_{i}", item)
                    elem.append(child)
            else:
                child = ET.Element(key)
                child.text = str(val)
                elem.append(child)
        return elem

    root = dict_to_xml(root_tag, json_obj)
    # Convert XML to a string and prettify it
    xml_str = ET.tostring(root, encoding='unicode')
    pretty_xml_str = minidom.parseString(xml_str).toprettyxml(indent="    ")
    return pretty_xml_str

def main():
    # Prompt user for the JSON file path
    json_file_path = input("Enter the path to the JSON file to be converted: ")

    # Check if the file has a .json extension
    if not json_file_path.lower().endswith('.json'):
        print("Error: The file does not have a .json extension.")
        return

    # Generate the XML file path with the same base name
    base_name = os.path.splitext(json_file_path)[0]
    xml_file_path = base_name + '.xml'

    try:
        # Read JSON data from the input file
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)
        
        # Convert JSON to XML
        xml_data = json_to_xml(json_data, 'Root')
        
        # Write XML data to the output file
        with open(xml_file_path, 'w') as xml_file:
            xml_file.write(xml_data)
        
        print(f"JSON data from {json_file_path} has been converted to XML and saved to {xml_file_path}")
    
    except FileNotFoundError:
        print(f"Error: The file {json_file_path} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The file {json_file_path} does not contain valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
