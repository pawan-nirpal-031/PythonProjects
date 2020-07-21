fn = input()
fh = open(fn)
c=0
for line in fh:
    if(line.startswith('From') and (not line.startswith('From:'))):
        c+=1
        x = line.split()
        print(x[1])


print('There were '+str(c)+' lines in the file with From as the first word')