import urllib.request as ureq,urllib.parse as upar,urllib.error as uerr 
from bs4 import BeautifulSoup
import time
try:
    t1 = time.time()
    url = input("Enter url :")
    html = ureq.urlopen(url).read()
    sp = BeautifulSoup(html,'html.parser')
    tags = sp('span')
    sum =0
    for t in tags:
        sum+=int(t.contents[0])
    print(sum)
    t2 = time.time()
    print(str(t2-t1))
except Exception:
    print('Unable to do it')

