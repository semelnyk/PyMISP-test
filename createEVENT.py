import argparse
from pymisp import ExpandedPyMISP, MISPEvent

# Add your MISP creds here
misp_url = "https://.com/"
misp_key = ""
misp_verifycert = True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create an event on MISP.')
    parser.add_argument("-d", "--distrib", type=int, help="The distribution setting used for the attributes and for the newly created event, if relevant. [0-3].")
    parser.add_argument("-i", "--info", default="Default event info", help="Used to populate the event info field if no event ID supplied.")
    parser.add_argument("-a", "--analysis", type=int, help="The analysis level of the newly created event, if applicable. [0-2]")
    parser.add_argument("-t", "--threat", type=int, help="The threat level ID of the newly created event, if applicable. [1-4]")
    args = parser.parse_args()

    misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)

    event = MISPEvent()
    event.distribution = args.distrib
    event.threat_level_id = args.threat
    event.analysis = args.analysis
    event.info = args.info

    event = misp.add_event(event, pythonify=True)
    print(event)
