#!/usr/bin/python3
"""Sends a request to a URL and displays the value of
the X-Request-Id variable."""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from the command-line arguments

    # Send a request to the URL
    with urllib.request.urlopen(url) as response:
        # Retrieve the value of the X-Request-Id header
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
