#!/usr/bin/python3
"""Fetches the body response from https://alx-intranet.hbtn.io/status."""

import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(response.text).__name__}")
    print(f"\t- content: {response.text}")
