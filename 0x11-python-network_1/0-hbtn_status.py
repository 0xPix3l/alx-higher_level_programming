#!/usr/bin/python3
""" fetches a url """
import urllib.request

if __name__ == "__main__":
    """fetches url"""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        html_str = html.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html_str))