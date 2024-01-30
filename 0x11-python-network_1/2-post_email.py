#!/usr/bin/python3
"""
send a post request in a url
"""

import sys
from urllib import *
if __name__ == "__main__" :
    data = {
        'email': sys.argv[2]
    }
    data = data.encode('ascii')
    url = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print('Your email is: {}'.format(body.decode('utf-8')))
