#!/usr/bin/python3
import requests
import sys

url = sys.argv[1]

response = requests.get(url)
body = response.text

if response.status_code >= 400:
    print("Error code: {}".format(response.status_code))
else:
    print(body)
