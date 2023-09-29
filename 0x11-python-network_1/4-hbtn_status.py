#!/usr/bin/python3
"""
Fetches the body response from https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    content_type = type(response.text).__name__
    content = response.text

    print("Body response:")
    print(f"    - type: {content_type}")
    print(f"    - content: {content}")
