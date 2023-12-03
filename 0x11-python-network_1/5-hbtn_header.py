#!/usr/bin/python3

"""displays the value of the variable
X-Request-Id in the response header"""

import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    value = r.headers['X-Request-Id']
    print(value)
