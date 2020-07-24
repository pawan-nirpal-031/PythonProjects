from urllib.error import URLError
import urllib.request as ureq,urllib.parse as upar,urllib.error as uerr 
fh = ureq.urlopen('http://data.pr4e.org/romeo.txt',)
fh2 = open('dork.html','w')
# pig = ''
# for line in fh:
#     wr = line.decode()
#     pig = pig+wr
# for line in fh2:
#     if(line.startswith()=='<p>'):
#         fh2.write(pig)
for line in fh:
    print(line.decode().strip())
