#!/usr/bin/python3
"""Sends a POST request with a given email to a specified URL
and displays the response body."""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={"email": email})
    print(response.text)
