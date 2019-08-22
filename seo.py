from urllib import request
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
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
    soup = BeautifulSoup(site,'html.parser')
    description = soup.find('meta',attrs={'name':'description'}) # que busque en el atributo name="description"
    site.close()
    print('description string : ',description.get('content'))
    sizeDescription = len(description.get('content'))
    print(f'The description size is {sizeDescription}')
    print('The description is less than 154' if sizeDescription < 154 else '')

def verifyTitle(URL):
    html = urlopen(URL)
    soup = BeautifulSoup(html.read(),'html.parser')
    # print(soup) imprime todo el html
    print(f'the size of the title content is {len(soup.html.head.title.string)}')
    print(f'the content of the title is {soup.html.head.title.string}')

def keywords(URL): #palabras clave de mayor densidad
    site = urlopen(URL)
    soup = BeautifulSoup(site,'html.parser')
    keyWords = soup.find('meta',attrs={'name':'keywords'})
    print(f'keywords {keyWords}')
    words = keyWords.get('content').split()
    # print(len(words))
    for word in words :
        print(f'the word {word} is repeated {len(soup.findAll(text=re.compile(word)))} times')
    
# check the alt attribute in the image tag
def checkTag(URL):
    site = urlopen(URL)
    soup = BeautifulSoup(site,'html.parser')
    for index,image in enumerate(soup.findAll('img')):
        print(f'Image image #{index+1}:',image["src"])
        print(f'Alt image #{index+1}',image.get('alt','None'))

def readH1(URL):
    site = urlopen(URL)
    soup = BeautifulSoup(site,'html.parser')
    for index,h1 in enumerate(soup.findAll('h1')):
        string = h1.string
        print(f'h1 #{index+1} string ',h1.string 
                if string is not None else 'no content')
        
def checkLinks(URL):
    site = urlopen(URL)
    soup = BeautifulSoup(site,'html.parser')
    # buscando todos los enlaces que tienen un href
    elements = soup.findAll('a') # soup.select('a')
    links = [link.get('href') for link in elements
                if link.get('href').startswith('http')]
    print(links)
    resultCode = {link:urlopen(link).code for link in links[:4]}
    print(resultCode)
    
def checkRobots(URL):
    site = urlopen(f'{URL}/robots.txt')
    if site.code != 200 :
        print('robots.txt file not found')
        return
    soup = BeautifulSoup(site)
    print(soup)

def checkFavicon(URL):
    page = urlopen(URL)
    soup = BeautifulSoup(page,'html.parser')
    icon_link = soup.find('link',rel='icon')
    icon = urlopen(URL+icon_link['href'])
    with open('test.ico','wb') as file:
        try:
            file.write(icon.read())
        except:
            print('icon not found')
            
def googleAnalytics(URL):
    site = urlopen(URL)
    soup = BeautifulSoup(site,'html.parser')
    if(soup.findAll(text=re.compile('.google-analytics'))):
        print('google-analytics')
        return
    print('not found google-analytics')

def language(URL):
    site = urlopen(URL)
    soup = BeautifulSoup(site,'html.parser')
    lang = soup.find('html')['lang']
    print(f'Language {lang}')

if __name__ == "__main__":
    URL = 'http://python.org'
    try:
        print(verifySSL(URL))
        print(verifyWWW(URL))
        print(pageSize(URL))
        comparisons(URL)
        verifyDescription(URL)
        verifyTitle(URL)
        keywords(URL)
        checkTag(URL)
        readH1(URL)
        checkLinks(URL)
        checkRobots(URL)
        checkFavicon(URL)
        googleAnalytics(URL)
        language(URL)
    except HTTPError as e:
        print('Err : status code', e.code)
    
    except URLError:
        print("Server down or incorrect domain")