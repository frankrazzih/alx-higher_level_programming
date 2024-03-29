#!/usr/bin/python3
"""
get the request id
"""

import sys
import urllib.request
if __name__ == "__main__":
    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print('{}'.format(response.headers.get('X-Request-Id')))
