"""
Modified example coming from:
Python Web Penetration Testing Cookbook.pdf

"""

import requests

verbs = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'TEST']
for verb in verbs:
    req = requests.request(verb, 'http://localhost:3000/#')
    print(verb, req.status_code, req.reason)
    if verb == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
        print('Possible Cross Site Tracing vulnerability found')

