#!/bin/bash
# Display the allowed HTTP methods for a server using curl.

# Send a HEAD request to retrieve the allowed HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
