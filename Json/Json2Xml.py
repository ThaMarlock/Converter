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
    # Example JSON data
    json_data = {
        "name": "John",
        "age": 30,
        "children": [
            {"name": "Alice", "age": 10},
            {"name": "Bob", "age": 5}
        ],
        "address": {
            "street": "123 Elm St",
            "city": "Somewhere"
        }
    }
    
    # Convert JSON to XML
    xml_data = json_to_xml(json_data, 'Person')
    
    # Print XML data
    print(xml_data)

if __name__ == "__main__":
    main()
