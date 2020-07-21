cnts = dict()
line = input('Enter a line : ')
words = line.split()

print(words)
c=0
for word in words:
    cnts[word] = cnts.get(word,0)+1

for key,val in cnts.items(): #convinent way to traverse through a dict
    print(key,val)

