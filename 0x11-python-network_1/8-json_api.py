#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with an optional letter.
Usage: ./8-json_api.py <letter>
  - The provided letter is sent as the value of the variable `q`.
  - If no letter is provided, sets `q` to an empty string.
"""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    
    try:
        user_data = response.json()
        if user_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(user_data.get("id"), user_data.get("name")))
    except ValueError:
        print("Invalid JSON response")
