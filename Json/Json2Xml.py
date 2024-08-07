import json
import xml.etree.ElementTree as ET

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
    return ET.tostring(root, encoding='unicode')

def main():
    # Define file paths
    json_file_path = 'input.json'  # Input JSON file path
    xml_file_path = 'output.xml'   # Output XML file path

    # Read JSON data from the input file
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    
    # Convert JSON to XML
    xml_data = json_to_xml(json_data, 'Root')
    
    # Write XML data to the output file
    with open(xml_file_path, 'w') as xml_file:
        xml_file.write(xml_data)
    
    print(f"JSON data from {json_file_path} has been converted to XML and saved to {xml_file_path}")

if __name__ == "__main__":
    main()
