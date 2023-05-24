from pymisp import ExpandedPyMISP
import argparse

import urllib3

urllib3.disable_warnings()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Delete your MISP Events from terminal")
    parser.add_argument("-e", "--event", help="Add the event(id) to be deleted")
    parser.add_argument("-a", "--attribute", help="Add the attribute(id) to be deleted")
    args = parser.parse_args()

    # Connection to misp instance
    misp_url = 'YOUR_URL'
    misp_key = 'YOUR_AUTHKEY'
    misp_verifycert = 0
    misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)



    # Checking whether the user added an event, an attribute, or both, and deletes
    if args.event and args.attribute:
        misp.delete_event(args.event)
        misp.delete_attribute(args.attribute)
        print("Event " + args.event + " and " + args.attribute + " deleted") 
    elif args.event:
        misp.delete_event(args.event)
        print("Event " + args.event + " deleted")
    elif args.attribute:
        misp.delete_attribute(args.attribute)
        print("Attribute " + args.attribute + " deleted")
