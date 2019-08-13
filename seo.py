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
    print(f'os.stat().st_size returns : ',os.stat('page.txt').st_size)
    
def verifyDescription(URL):
    site = request.urlopen(URL)
    soup = BeautifulSoup(site)
    description = soup.find('meta',attrs={'name':'description'})
    sizeDescription = len(description.get('content'))
    print(f'The description size is {sizeDescription}')
    print('The description is less than 154' if sizeDescription < 154 else '')

def verifyTitle(URL):
    pass

if __name__ == "__main__":
    URL = 'http://python.org'
    print(verifySSL(URL))
    print(verifyWWW(URL))
    print(pageSize(URL))
    comparisons(URL)
    verifyDescription(URL)
