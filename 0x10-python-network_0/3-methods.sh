#!/bin/bash
# This script displays the HTTP methods accepted by a server for a given URL.
curl -sI "$1" | grep "Allow" | awk '{print $2, $3, $4}'
