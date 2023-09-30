#!/usr/bin/python3
"""
Sends a request to a specified URL and displays the response body.
"""

import requests
from sys import argv


def main(argv):
    """
    Handles HTTP errors and prints the HTTP status code in case of an error.
    """
    url = argv[1]
    response = requests.get(url)

    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))


if __name__ == "__main__":
    main(argv)
