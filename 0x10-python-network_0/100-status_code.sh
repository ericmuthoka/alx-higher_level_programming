#!/bin/bash
#sends a request to a URL passed as an argument, and displays only the response status code
curl -s -w "%{http_code}" "$1"
