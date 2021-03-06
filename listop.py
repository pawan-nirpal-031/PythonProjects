arr = list()

n = int(input('Enter no of elements'))
for i in range(n):
    x = int(input())
    arr.append(x)

cpyarr = arr.copy()
print("list copied in  cpyarr")

arrx = arr.copy()
arr.clear()
print('list cleared')

arr1 = arrx.copy()
arr1.sort()
print('arr1 sorted')
print(arr1)

arr1.pop()
print('last element popped')
print(arr1)

cnt_elm = int(input('Enter the element to check for count'))
print("count of "+str(cnt_elm)+" is "+str(arrx.count(cnt_elm)))

arr2 = arrx.copy()
arr2.reverse()
print('arr2 is reversed arr')
print(arr2)

ins_el = (input('Enter element to be inserted and positon').split())
arr3 = arrx.copy()
arr3.insert(int(ins_el[1]),int(ins_el[0]))
print(arr3)

indx = int(input('Get the index of which element'))
print('index of '+str(indx)+' is '+str(arrx.index(indx)))

print('Extending arrx into arr3')
arrx.extend(arr3)

print(arrx)