from pymisp import MISPEvent, ExpandedPyMISP
import argparse

import urllib3

urllib3.disable_warnings()





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create MISP events from terminal')
    parser.add_argument("-i", "--info", required=True, help="A string defining the event")
    parser.add_argument("-d", "--distribution", required=True, help="Select the desired distribution option, 0 = Your organisation only, 1 = This community only, 2 = Connected communities, 3 = All communities")
    parser.add_argument("-l", "--thread", required=True, help="Select the desired threat level, 1 = High, 2 = Medium, 3 = Low, 4 = Undefined")
    parser.add_argument("-a", "--analysis", required=True, help="Select the actual analysis stage, 0 = Initial, 2 = Ongoing, 3 = Completed")
    parser.add_argument("-t", "--time", required=True, help="Add the time the event was discovered, format is YYYY-MM-DD")


    args = parser.parse_args()




    # Connection to MISP instance
    
    misp_url = 'https://10.0.2.8'
    misp_key = 'knvLrZVV6cG4Mw0GSEne2zxpuLnK33qOyuDZmNjZ'
    misp_verifycert = 0
    misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)

    # Temporal object that stores values from the arguments

    event_to_send = MISPEvent()
    event_to_send.info = args.info
    event_to_send.distribution = args.distribution
    event_to_send.threat_level_id = args.thread
    event_to_send.analysis = args.analysis
    event_to_send.set_date(args.time)

    # Actual event creation
    event = misp.add_event(event_to_send, pythonify=True)
    event_id = event.id
    print("Event id: %s" % event_id)
