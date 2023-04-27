import argparse
from io import open
from pymisp import PyMISP

# Add your MISP URL and API key here
misp_url = "https://misp.intelfp.com/"
misp_key = "yX7JeRrt8qSUoN8byopev4xkmACJwdEfHtT85q4q"
misp_verifycert = True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Update a MISP event.")
    parser.add_argument("-e", "--event", required=True, help="Event ID to update.")
    parser.add_argument("-i", "--input", required=True, help="Input file")
    args = parser.parse_args()
    pymisp = PyMISP(misp_url, misp_key, misp_verifycert)
    with open(args.input, 'r') as f:
        result = pymisp.freetext(args.event, f.read())
    print(result)