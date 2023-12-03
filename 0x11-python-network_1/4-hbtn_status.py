#!/usr/bin/python3

"""fetches https://alx-intranet.hbtn.io/status"""

import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    data = r.content.decode("UTF-8")
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
