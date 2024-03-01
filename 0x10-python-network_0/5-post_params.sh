#!/bin/bash
# Sends a POST request to a URL with custom parameters and displays the body of the response

url=$1
email="test@gmail.com"
subject="I will always be here for PLD"

curl -s -X POST -d "email=$email" -d "subject=$subject" "$url"
