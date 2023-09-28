#!/bin/bash
# This script sends a request to the given URL and displays the size of the response body in bytes.

if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url=$1
response=$(curl -sI "$url" | grep -i 'Content-Length' | awk '{print $2}')
echo "Size of the response body: $response bytes"
