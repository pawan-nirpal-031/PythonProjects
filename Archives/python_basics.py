'''
ROLL NO : TECOC341
NAME : Pawan Nirpal

'''


nint = int(input('Enter an Integer '))
print('You Entred an int '+str(type(nint))+str(nint))

nfloat = float(input('Enter a float value '))
print('You Entred a float '+str(type(nfloat))+str(nfloat))

nstring = input('Enter a string ')
print('You entred a string  '+nstring)

nchar = input('Input a character ')
print('You entred a char  '+nchar)

if nint>10:
    print('You entred an Int greater than 10 , this demos if statement')
elif nint>0 and nint<10:
    print('You entred a decimal digit 0-9 , this demos elif statement')

print('For loop from 1 to n')
for i in range(1,nint+1):
    print(str(i))

i =1
print('while loop from 1 to n')
while(i<=nint):
    print(str(i))
    i+=1

sq = int(input('Enter an integer calulates squres from 1 to n'))
def sqrs(sq):
    for i in range(1,sq+1):
        print(str(i)+' sqre : '+str(i*i))

sqrs(sq)

a,b,c = input('Enter three ints to check for maximum using lambda fun').split()
lmd = lambda x,y,z : max(x,max(y,z))

print(lmd(a,b,c))






