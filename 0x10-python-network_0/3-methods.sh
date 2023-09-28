#!/bin/bash
# This script fetches the allowed HTTP methods for a given URL.
# Usage: ./3-methods.sh <URL>

# Retrieve the URL from the user.
URL=$1

# Send an HTTP HEAD request to the specified server and extract the allowed methods.
curl -sI "$URL" | grep "Allow" | awk '{print $2, $3, $4}'

