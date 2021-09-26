import argparse
import json
import sys
import traceback

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pulls IP addresses from a Shodan JSON and optionally excludes IPs '
                                                 'from specified countries.')
    parser.add_argument('file', metavar='[JSON file]', type=str, nargs=1, help='Location of the Shodan JSON file')
    parser.add_argument('--exclude-country', nargs='+', default=[], help='List countries to exclude. For example: CN, '
                                                                         'RU, UK would be China, Russia and the '
                                                                         'United Kingdom')
    args = parser.parse_args()

    entries = []
    with open(args.file[0], 'r') as json_file:
        json_data = json_file.readlines()
    for json_object in json_data:
        entries.append(json.loads(json_object))

    present_country_codes = set()

    for entry in entries:
        try:
            present_country_codes.add(entry['location']['country_code'].lower())
        except AttributeError:
            pass

    valid_country_codes = present_country_codes.copy()
    for country in args.exclude_country:
        try:
            valid_country_codes.remove(country.lower())
        except KeyError:
            print("The country code " + country + " is not present in the JSON file. Valid country codes:",
                  file=sys.stderr)
            for country_code in present_country_codes:
                print(country_code.upper(), file=sys.stderr)

    unknown_country_ips = []

    for entry in entries:
        try:
            if entry['location']['country_code'].lower() in valid_country_codes:
                print(entry['ip_str'])
        except AttributeError as exception:
            if entry['location']['country_code'] is None:
                unknown_country_ips.append(entry['ip_str'])
            else:
                print("An unknown error occurred. Please contact the developer with the error below:", file=sys.stderr)
                print(''.join(traceback.TracebackException.from_exception(exception).format()), file=sys.stderr)

    print('\nPrinting IPs from unknown countries:')

    for ip in unknown_country_ips:
        print(ip)
