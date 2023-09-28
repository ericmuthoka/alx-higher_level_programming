#!/bin/bash
# This script displays the HTTP methods accepted by a server for a given URL.

# Check if the user provided a URL
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send an OPTIONS request to the specified URL and display the allowed methods
allowed_methods=$(curl -sI -X OPTIONS "$1" | awk -F ": " '/Allow/ {print $2}')

# Display the allowed HTTP methods
echo "HTTP Methods allowed for $1:"
echo "$allowed_methods"

