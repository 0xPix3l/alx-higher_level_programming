#!/usr/bin/python3
""" fetches a url """
import urllib.request

if __name__ == "__main__":
    """ fetches a url """
    with urllib.request.urlopen('https://www.example.com') as response:
        html = response.read()
        html_str = html.decode('utf-8')

print("Body response:")
print("\t- type: {}".format(type(html)))
print("\t- content: {}".format(html))
print("\t- utf8 content: {}".format(html_str))
