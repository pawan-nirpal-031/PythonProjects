fh = open("dork.html",'w')
fh2 = open('webSrcaping.txt')
for line in fh2:
    if(line.startswith('<')):
        fh.write(line)