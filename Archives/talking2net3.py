from urllib.error import URLError
import urllib.request as ureq,urllib.parse as upar,urllib.error as uerr 
fh = ureq.urlopen('http://data.pr4e.org/romeo.txt',)
cnts = dict()
for line in fh:
    words = line.decode().split()
    for wrd in words:
        cnts[wrd] = cnts.get(wrd,0)+1
print(cnts)
