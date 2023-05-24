from pymisp import ExpandedPyMISP, MISPAttribute
import argparse

import urllib3

urllib3.disable_warnings()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Update your MISP Events from terminal")
    parser.add_argument("-e", "--event", required=True, help="Add the event to be updated")
    parser.add_argument("-t", "--type", required=True, help="Add a type to the attribute")
    parser.add_argument("-v", "--value", required=True, help="Add a value to the attribute")
    parser.add_argument("-c", "--category", required=True, help="Add a category to the attribute")
    parser.add_argument("-i", "--id", required=True, help="State if you want to send it to IDS")

    args = parser.parse_args()


    # Check if id and publish arguments are Y or N, as it will be used later as a condition
    if args.id != "Y" or args.id != "N":
            print("To IDS must be Y for Yes or N for No")
            exit(0)

    # Connection to instance
    misp_url = 'YOUR_URL'
    misp_key = 'YOUR_AUTHKEY'
    misp_verifycert = 0
    misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)

    # Object to store values from arguments
    attribute_to_add = MISPAttribute()
    attribute_to_add.type = args.type
    attribute_to_add.value = args.value
    attribute_to_add.category = args.category

    # Conditional to send to IDS
    if args.id == "Y":
        attribute_to_add.to_ids = True
    else:
        attribute_to_add.to_ids = False

    attribute = misp.add_attribute(args.event, attribute_to_add, pythonify=True)

    print("Attribute added to event " + args.event)
    
        
    