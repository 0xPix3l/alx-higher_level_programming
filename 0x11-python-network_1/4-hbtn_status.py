#!/usr/bin/python3
""" fetch """
import requests


if __name__ = "__main__":
    """ fetches a website """
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
