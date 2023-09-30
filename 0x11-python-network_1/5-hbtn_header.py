#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a specified URL.
Usage: ./5-hbtn_header.py <URL>
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-Id")
    print(x_request_id)
