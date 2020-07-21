fn = input('Enter the file name : ')
fh = open(fn)
count =dict()
for line in fh:
    if(line.startswith('From ')):
        words = line.split()
        time = words[5]
        count[time[:time.find(':')]] = count.get(time[:time.find(':')],0)+1

l = list(count.items())
l.sort()
for k,v in l:
    print(k,v)


