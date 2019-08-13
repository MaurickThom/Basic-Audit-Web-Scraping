from urllib import request
import os
from bs4 import BeautifulSoup

def verifySSL(URL):
    req = request.Request(URL)
    result = request.urlopen(req)
    return result.geturl()

def pageSize(URL):
    site = request.urlopen(URL)
    meta = site.info()
    try:
        return {f'Content-Length of {site.geturl()}':site.headers['content-length']}
    finally:
        site.close()

def verifyWWW(URL):
    req = request.Request(URL)
    result = request.urlopen(req)
    return result.geturl()

def comparisons(URL):
    site = request.urlopen(URL)
    meta = site.info() # metadata HTML
    file = open('page.txt','wb')
    file.write(site.read())
    site.close()
    file.close()
    file = open('page.txt','r')
    print(f'File on disk after download {len(file.read())}')
    file.close()
    print(f'os.stat().st_size returns : ',os.stat('out.txt').st_size)

if __name__ == "__main__":
    URL = 'http://python.org'
    print(pageSize(URL))
    comparisons(URL)