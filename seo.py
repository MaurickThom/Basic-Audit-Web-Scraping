from urllib import request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import re

def verifySSL(URL):
    # req = request.Request(URL)
    # result = request.urlopen(req)
    result = urlopen(URL)
    return result.geturl()

def pageSize(URL):
    # site = request.urlopen(URL)
    site = urlopen(URL)
    meta = site.info()
    print(f'Meta :  \n{meta}')
    try:
        return {f'Content-Length of {site.geturl()}':site.headers['content-length']}
    finally:
        site.close()

def verifyWWW(URL):
    # req = request.Request(URL)
    # result = request.urlopen(req)
    result = urlopen(URL)
    return result.geturl()

def comparisons(URL):
    # site = request.urlopen(URL)
    site = urlopen(URL)
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
    # site = request.urlopen(URL)
    site = urlopen(URL)
    soup = BeautifulSoup(site)
    description = soup.find('meta',attrs={'name':'description'}) # que busque en el atributo name="description"
    site.close()
    print('description string : ',description.get('content'))
    sizeDescription = len(description.get('content'))
    print(f'The description size is {sizeDescription}')
    print('The description is less than 154' if sizeDescription < 154 else '')

def verifyTitle(URL):
    html = urlopen(URL)
    soup = BeautifulSoup(html.read())
    # print(soup) imprime todo el html
    print(f'the size of the title content is {len(soup.html.head.title.string)}')
    print(f'the content of the title is {soup.html.head.title.string}')

def keywords(URL): #palabras clave de mayor densidad
    site = urlopen(URL)
    soup = BeautifulSoup(site)
    keyWords = soup.find('meta',attrs={'name':'keywords'})
    print(f'keywords {keyWords}')
    words = keyWords.get('content').split()
    # print(len(words))
    for word in words :
        print(f'the word {word} is repeated {len(soup.findAll(text=re.compile(word)))} times')
    
# check the alt attribute in the image tag
def checkTag(URL):
    site = urlopen(URL)
    soup = BeautifulSoup(site)
    count = 1
    for image in soup.findAll('img'):
        print(f'Image image #{count}:',image["src"])
        print(f'Alt image #{count}',image.get('alt','None'))
        count+=1

def readH1(URL):
    site = urlopen(URL)
    soup = BeautifulSoup(site)
    count = 1
    for h1 in soup.findAll('h1'):
        string = h1.string
        print(f'h1 #{count} string ',h1.string if string is not None else 'no content')
        count+=1

if __name__ == "__main__":
    URL = 'http://python.org'
    print(verifySSL(URL))
    print(verifyWWW(URL))
    print(pageSize(URL))
    comparisons(URL)
    verifyDescription(URL)
    verifyTitle(URL)
    keywords(URL)
    checkTag(URL)
    readH1(URL)
