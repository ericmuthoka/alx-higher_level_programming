#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter
and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    # Send a POST request with the email as a parameter
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print("Your email is: {}".format(body))
