import urllib.request as ureq,urllib.parse as upar,urllib.error as uerr 
from bs4 import BeautifulSoup
 


try:
    fh = open('links.txt','w')
    url = 'http://'+input('Enter website : ')
    html = ureq.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    for tg in tags:
        # print('tag : ',tg)
        # print('URL fetched : ',tg.get('href',None))
        # print('Contents: ',tg.contents[0])
        # print('Attrs : ',tg.attrs)
        fh.write('URL fetched : '+tg.get('href',None)+'\n')
        # fh.write('Contents: ',tg.contents[0])
        
except Exception as e:
    print('Action prohibited \n:-(','Quitting this request')
    print(e.with_traceback)

