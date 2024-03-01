#!/usr/bin/python3
import requests
import sys

url = sys.argv[1]

response = requests.get(url)
header = response.headers.get('X-Request-Id')

print(header)
