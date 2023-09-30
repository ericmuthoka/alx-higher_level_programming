#!/usr/bin/python3
"""
Uses the GitHub API to retrieve and display a GitHub user ID
based on provided credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Utilizes Basic Authentication for accessing the user ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Set up Basic Authentication with provided credentials
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    # Send a request to GitHub API to retrieve user data
    response = requests.get("https://api.github.com/user", auth=auth)

    # Print the GitHub user ID from the response
    print(response.json().get("id"))
