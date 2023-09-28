#!/bin/bash
# This script fetches the allowed HTTP methods for a given URL.
curl -sI "$URL" | grep "Allow" | awk '{print $2, $3, $4}'

