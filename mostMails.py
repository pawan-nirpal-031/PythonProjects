fn = input('Enter the file name :')
fh = open(fn)
count = dict()
maxMails =0
hisName =None
for line in fh:
    if(line.startswith('From ')):
        words = line.split()
        count[words[1]] = count.get(words[1],0)+1

for key,val in count.items():
    if(count[key]>maxMails):
        maxMails = count[key]
        hisName = key

# print(hisName,maxMails)
print(count)