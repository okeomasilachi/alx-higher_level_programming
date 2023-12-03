#!/usr/bin/python3


""" sends a request to the URL and displays
the body of the response."""

import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        value = r.content.decode("UTF-8")
    print(value)
