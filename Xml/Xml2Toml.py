import xmltodict
import toml
import os

def convert_xml_to_toml(xml_path):
    try:
        # Read the XML file
        with open(xml_path, 'r') as xml_file:
            xml_content = xml_file.read()

        # Convert XML to a Python dictionary
        xml_dict = xmltodict.parse(xml_content)

        # Convert the Python dictionary to a TOML string
        toml_content = toml.dumps(xml_dict)

        # Get the output TOML file path
        toml_path = os.path.splitext(xml_path)[0] + '.toml'

        # Write the TOML content to a file
        with open(toml_path, 'w') as toml_file:
            toml_file.write(toml_content)

        print(f"TOML file created successfully: {toml_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Ask the user for the path to the XML file
    xml_path = input("Please enter the path to the XML file: ")
    
    if os.path.isfile(xml_path):
        convert_xml_to_toml(xml_path)
    else:
        print("The provided path does not point to a valid file.")

if __name__ == "__main__":
    main()
