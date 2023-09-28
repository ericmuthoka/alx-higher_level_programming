#!/bin/bash
# This script displays all HTTP methods the server will accept for a given URL.

# Check if the user provided a URL
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send an OPTIONS request to the specified URL and display the allowed methods
allowed_methods=$(curl -sI -X OPTIONS "$1" | awk -F ": " '/Allow/ {print $2}')
echo "$allowed_methods"

