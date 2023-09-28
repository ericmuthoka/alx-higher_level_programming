#!/bin/bash
# This script retrieves the size of the response body in bytes for a given URL using curl.

# Check if the user provided a URL
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a GET request to the specified URL and display the size of the response body
response_size=$(curl -sI "$1" | awk '/Content-Length/{print $2}')
echo "$response_size"
