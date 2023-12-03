#!/usr/bin/python3

"""
sends a request to the URL and
displays the body of the response"""

from sys import argv
from urllib import request, error


if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as res:
            data = res.read()
            print(data.decode('UTF-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
