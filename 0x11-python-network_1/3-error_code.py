#!/usr/bin/python3
"""
Takes url
"""
import urllib.request
from sys import argv

if __name == "__main__":
    """
    takes url
    """
    url = argv[1]
    req = urllib.requset.Request(url)
    try:
        wih urllib.request.urlopen(req) as response:
            html = response.read()
            html_str = html.decode('utf-8')
            print(html_str)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

