from urllib import request

def verifySSL(URL)->bool:
    req = request.Request(URL)
    result = request.urlopen(req)
    return result

if __name__ == "__main__":
    print(verifySSL('http://python.org'))