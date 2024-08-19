import xmltodict
import csv
import os

def convert_xml_to_csv(xml_path):
    try:
        # Read the XML file
        with open(xml_path, 'r') as xml_file:
            xml_content = xml_file.read()

        # Convert XML to a Python dictionary
        xml_dict = xmltodict.parse(xml_content)

        # Assuming that the XML file contains a list of items, we'll need to find the appropriate level in the dictionary
        # This part might need to be adapted based on the specific structure of the XML file
        root_element = list(xml_dict.keys())[0]
        items = xml_dict[root_element]

        if isinstance(items, dict):
            items = [items]  # If there's only one item, convert it to a list of one item

        # Get the output CSV file path
        csv_path = os.path.splitext(xml_path)[0] + '.csv'

        # Writing to CSV
        with open(csv_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)

            # Extract headers based on the keys in the first item
            headers = items[0].keys()
            writer.writerow(headers)

            # Write each item to the CSV file
            for item in items:
                writer.writerow(item.values())

        print(f"CSV file created successfully: {csv_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Ask the user for the path to the XML file
    xml_path = input("Please enter the path to the XML file: ")
    
    if os.path.isfile(xml_path):
        convert_xml_to_csv(xml_path)
    else:
        print("The provided path does not point to a valid file.")

if __name__ == "__main__":
    main()
