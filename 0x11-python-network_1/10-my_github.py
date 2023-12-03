#!/usr/bin/python3

"""
akes your GitHub credentials
(username and password) and uses
the GitHub API to display your id"""

import requests
import sys


if __name__ == "__main__":
    uname = sys.argv[1]
    passwd = sys.argv[2]

    url = "https://api.github.com/user"
    auth = (uname, passwd)

    res = requests.get(url, auth=auth)

    try:
        j = res.json()
        uid = j.get('id')
        print("{}".format(uid))
    except ValueError:
        print("Not a valid JSON")
