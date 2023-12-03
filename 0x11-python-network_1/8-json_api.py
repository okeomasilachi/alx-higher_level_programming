#!/usr/bin/python3

"""
sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter."""

import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) <= 1:
        p = {'q': ""}
    else:
        p = {'q': sys.argv[1]}
    r = requests.post(url, data=p)
    try:
        j = r.json()
        if j:
            print(f"[{j['id']}] {j['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
