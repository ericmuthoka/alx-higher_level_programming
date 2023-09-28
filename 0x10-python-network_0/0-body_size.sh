#!/bin/bash
# This script retrieves the Content-Length of a given IP address using curl and awk.

# Check if the user provided an IP address
if [ -z "$1" ]; then
  echo "Usage: $0 <IP_address>"
  exit 1
fi

# Send a HEAD request to the specified IP address and retrieve the Content-Length
content_length=$(curl -sI "$1" | awk '/Content-Length/{print $2}')

# Check if Content-Length was found
if [ -z "$content_length" ]; then
  echo "Content-Length not found for the given IP address."
else
  echo "Content-Length of the response: $content_length bytes"
fi
