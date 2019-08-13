from urllib import request

def verifySSL(URL):
    req = request.Request(URL)
    result = request.urlopen(req)
    return result.geturl()

def pageSize(URL):
    site = request.urlopen(URL)
    meta = site.info()
    return {f'Content-Length of {site.geturl()}':site.headers['content-length']}

if __name__ == "__main__":
    print(pageSize('http://python.org'))