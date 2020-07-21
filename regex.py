import re
fh = open('mbox-short.txt')
for line in fh:
    # if(re.search('^From:',line.rstrip())):
    #     print(line)
    x = line.split();
    print(re.findall(['0-9+'],x))