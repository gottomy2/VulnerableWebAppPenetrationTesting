"""
Modified example coming from:
Python Web Penetration Testing Cookbook.pdf
"""

import requests


req = requests.get('http://localhost:3000/#')
headers = ['Server', 'Date', 'Via', 'X-Powered-By', 'X-Country-Code']


for header in headers:
    try:
        result = req.headers[header]
        print('%s: %s' % (header, result))
    except Exception as error:
        print('%s: Not found' % header)
