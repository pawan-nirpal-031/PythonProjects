# Assingment Word Count 
# Name : Pawan Nirpal , TECO341

txt = input().split() 
ht = dict()
for word in txt:
    ht[word] = ht.get(word,0)+1
print(ht)
