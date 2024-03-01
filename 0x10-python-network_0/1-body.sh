#!/bin/bash
# Sends a GET request to a URL and displays the body of the response (if status code is 200)

url=$1
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")

if [ "$status_code" -eq 200 ]; then
    curl -s "$url"
fi
