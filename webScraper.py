import urllib.request as ureq,urllib.parse as upar,urllib.error as uerr 
from bs4 import BeautifulSoup

try:
    url = 'http://'+input('Enter website : ')
    html = ureq.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    for tg in tags:
        print('tag : ',tg)
        print('URL fetched : ',tg.get('href',None))
        print('Contents: ',tg.contents[0])
        print('Attrs : ',tg.attrs)
        
except Exception:
    print('Action prohibited \n:-(','Quitting this request')
