from urllib import request

def verifySSL(URL):
    req = request.Request(URL)
    result = request.urlopen(req)
    return result.geturl()

if __name__ == "__main__":
    print(verifySSL('http://python.org'))