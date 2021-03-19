import hashlib
import requests
from bs4 import BeautifulSoup

def Get_Flag(emdee_url):
    req = requests.session()
    res = req.get(emdee_url)
    soup = SOUP(res.content)
    MD5 = soup.find_all('h3', align='center')[0].text
    # print(MD5)
    HASH = hashlib.md5(MD5.encode('utf-8')).hexdigest()
    data = {'hash': HASH}
    soup = SOUP(req.post(emdee_url, data).text)
    flag = soup.find_all('p',align="center")[0].text
    return flag

def SOUP(response_content):
    soup = BeautifulSoup(response_content, "html.parser")
    return soup

def run():
    while 1:
        emdee_addr = "http://206.189.121.131:31590/"
        flag = Get_Flag(emdee_addr)
        if flag:
            print(G + "[^_^]Get emdee Flag：%s!!!" % flag + E)
            break
        else:
            print(G + "[+]Fetching flag, please wait..." + E)
            continue


if __name__ == '__main__':
    G = '\033[32m'
    B = '\033[34m'
    E = '\033[0m'
    run()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    