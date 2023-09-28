#!/bin/bash
# This script displays the HTTP methods accepted by a server for a given URL.

# Check if the user provided a URL
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a HEAD request to the specified URL and display the allowed methods
curl -sI -X HEAD "$1" | awk '/Allow/ {print "HTTP Methods allowed for", "'"$1"'":", $2, $3, $4"}'

