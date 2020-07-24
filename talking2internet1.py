import socket as sk
import time 

fh = open('webSrcaping.txt','w')
t1 = time.time()
mysk=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
mysk.connect(('data.pr4e.org',80))
cmd = '''GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'''.encode()
mysk.send(cmd)

while(True):
    data = mysk.recv(512)
    if(len(data)<1):
        break
    
    print(data.decode())
    fh.write(data.decode())
mysk.close()
t2 = time.time()
print("your program took : ",str(t2-t1)," time to execute")