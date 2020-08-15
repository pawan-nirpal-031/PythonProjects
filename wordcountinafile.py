fh = open('romeo.txt')
ht = dict()
for line in fh:
    for word in line.split():
        ht[word] = ht.get(word,0)+1
print(ht)