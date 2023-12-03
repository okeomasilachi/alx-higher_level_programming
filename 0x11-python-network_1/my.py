
from urllib import request
import urllib
"""
with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
   html = res.read()
   print(f'\t- type: {type(html)}')
   print(f'\t- conteent: {html}')
   print(f'\t- utf8 content: {html.decode("UTF-8")}')
"""

"""
with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
   html = res.headers['X-Request-Id']
   print(html)
"""

data = urllib.parse.urlencode({'email': "hr@holbertonschool.com"})
data = data.encode('utf-8')
with request.Request('http://0.0.0.0:5000/post_email', data=data, method='POST') as s:
   see inm
   print(see)
