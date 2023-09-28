#!/bin/bash
# This script sends a request to the given URL and displays the size of the response body in bytes.

curl -sI "$1" | awk '/Content-Length/{print $2}'
