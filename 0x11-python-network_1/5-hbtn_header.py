#!/usr/bin/python3

"""displays the value of the variable
X-Request-Id in the response header"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    value = r.headers['X-Request-Id']
    print(value)
