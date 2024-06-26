#!/usr/bin/python3
"""
sends a post
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) < 2 else sys.argv[1]
    data = {"q": letter}
    r = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
