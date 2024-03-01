#!/bin/bash
# Sends a GET request to a URL with a custom header and displays the body of the response

url=$1
curl -s -H "X-School-User-Id: 98" "$url"
