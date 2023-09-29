#!/usr/bin/python3
"""Fetches the body response from https://alx-intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- Type: {}".format(type(body)))
        print("\t- Content: {}".format(body))
        print("\t- UTF-8 Content: {}".format(body.decode("utf-8")))
