#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body
curl -sX GET $1 -L
