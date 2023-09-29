#!/usr/bin/python3
"""Sends a request to a URL and displays the value of the
X-Request-Id variable in the response header."""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from the command-line arguments

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id:
        print(f"X-Request-Id: {x_request_id}")
    else:
        print("No X-Request-Id found in the response headers.")
