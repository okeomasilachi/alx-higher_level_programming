#!/usr/bin/python3

"""Gets the sha and author of
the first 10 commits of a user"""


import requests
import sys


if __name__ == "__main__":
    owner = sys.argv[1]
    repo = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    arg = {'per_page': 10}

    res = requests.get(url, params=arg)

    try:
        j = res.json()
        for data in j:
            key = data['sha']
            author = data['commit']['author']['name']
            print(f"{key}: {author}")
    except ValueError:
        print("Not a valid JSON")
