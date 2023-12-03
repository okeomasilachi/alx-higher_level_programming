#!/usr/bin/python3

"""Module fetches https://alx-intranet.hbtn.io/status"""


from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()
        print("Body response")
        print(f'\t- type: {type(html)}')
        print(f'\t- content: {html}')
        print(f'\t- utf8 content: {html.decode("UTF-8")}')
