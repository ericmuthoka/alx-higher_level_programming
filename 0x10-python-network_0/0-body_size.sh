#!/bin/bash
# This script retrieves the size of the response body in bytes for a given URL using curl.
curl -s "$1" | wc -c
