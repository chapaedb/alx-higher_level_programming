#!/bin/bash
# Displays all HTTP methods accepted by a server for a URL

url=$1
curl -s -I "$url" | grep -i Allow | cut -d' ' -f2-
