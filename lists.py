fname = input()
fh = open(fname)
ans =[]
for line in fh:
    x = line.split()
    for word in x:
        if(word not in ans):
            ans.append(word)

ans.sort()
print(ans)