import xmltodict
import yaml
import os

def convert_xml_to_yaml(xml_path):
    try:
        # Read the XML file
        with open(xml_path, 'r') as xml_file:
            xml_content = xml_file.read()

        # Convert XML to a Python dictionary
        xml_dict = xmltodict.parse(xml_content)

        # Convert the Python dictionary to a YAML string
        yaml_content = yaml.dump(xml_dict, default_flow_style=False)

        # Get the output YAML file path
        yaml_path = os.path.splitext(xml_path)[0] + '.yaml'

        # Write the YAML content to a file
        with open(yaml_path, 'w') as yaml_file:
            yaml_file.write(yaml_content)

        print(f"YAML file created successfully: {yaml_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Ask the user for the path to the XML file
    xml_path = input("Please enter the path to the XML file: ")
    
    if os.path.isfile(xml_path):
        convert_xml_to_yaml(xml_path)
    else:
        print("The provided path does not point to a valid file.")

if __name__ == "__main__":
    main()
