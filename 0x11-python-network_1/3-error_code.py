#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """
    takes in a URL and an email, sends a POST request to the passed
    """
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            html_str = html.decode('utf-8')
            print(html_str)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
