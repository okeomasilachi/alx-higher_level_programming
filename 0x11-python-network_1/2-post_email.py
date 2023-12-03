#!/usr/bin/python3

"""
sends a POST request to the passed
URL with the email as a parameter"""

from sys import argv
from urllib import parse, request

if __name__ == "__main__":
    url = argv[1]
    val = {'email': argv[2]}
    data = parse.urlencode(val)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as res:
        page = res.read()
        print(page.decode("UTF-8"))
