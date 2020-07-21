name = input()
fh = open(name)
c =0
ans =0
for line in fh:
    if(line.startswith('X-DSPAM-Confidence:')):
        c = c+1
        ans += float(line[line.find('0'):])
print('Average spam confidence: '+str(ans/c))
