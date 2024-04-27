#!/usr/bin/python3
""" fetches smth """
import requests
from sys import argv


if __name__ == "__main__":
    """ test """
    r = requests.get(argv[1])
    r_id = r.headers.get("X-Request-Id")
    print(r_id)
