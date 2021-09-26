# Shodan IP Parser

This is a quick script I wrote that allows you to parse Shodan IPs from a JSON export. Optionally, it allows you to exclude countries also.

## Usage

```
usage: shodan_parser.py [-h]
                        [--exclude-country EXCLUDE_COUNTRY [EXCLUDE_COUNTRY ...]]
                        [JSON file]

Pulls IP addresses from a Shodan JSON and optionally excludes IPs from
specified countries.

positional arguments:
  [JSON file]           Location of the Shodan JSON file

optional arguments:
  -h, --help            show this help message and exit
  --exclude-country EXCLUDE_COUNTRY [EXCLUDE_COUNTRY ...]
                        List countries to exclude. For example: CH, RU, UK
                        would be China, Russia and the United Kingdom

Process finished with exit code 0

```