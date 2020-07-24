import urllib.request as ureq,urllib.parse as upar,urllib.error as uerr 
fh = ureq.urlopen('http://www.dr-chuck.com/page1.htm')
wr = open('next.html','w')
for line in fh:
    print(line.decode().strip())
    wr.write(line.decode())