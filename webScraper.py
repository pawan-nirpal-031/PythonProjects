import urllib.request as ureq,urllib.parse as upar,urllib.error as uerr 
from bs4 import BeautifulSoup

try:
    url = 'http://'+input('Enter website : ')
    html = ureq.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    fileh = open('linksInGoogle.txt','w')
    print(soup)
    for tg in tags:
        print(tg.get('href',None))
        
except Exception:
    print('Action prohibited \n:-(','Quitting this request')
