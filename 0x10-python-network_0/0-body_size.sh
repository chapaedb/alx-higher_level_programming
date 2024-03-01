#!/bin/bash
# Sends a request to a URL and displays the size of the response body

url=$1
curl -sI "$url" | grep -i Content-Length | awk '{print $2}'
