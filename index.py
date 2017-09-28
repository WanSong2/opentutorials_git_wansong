# -*- coding: utf-8 -*-

pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:14]
print(num)


pin = "881120-1068234"
spl = pin.split('-')[1]
print(spl[0])

temp = 0
a = [1,3,5,4,2]
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j+1] > a[j]:
            temp = a[j+1]
            a[j+1] = a[j]
            a[j] = temp
print(a)


a = ['Life', 'is', 'too', 'short']
result = a[0] +' '+ a[1] +' '+ a[2] +' '+ a[3]
print(result)


a = (1, 2, 3)
a = (1, 2, 3, 4)
print(a)


a = {'A':90, 'B':80, 'C':70}
result = {'A':90, 'C':70}
print(result)
print(a['B'])


a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
print(aSet)


a = b = [1,2,3]
a[1] = 4
print(b)

a = 'a' in ('a', 'b', 'c')
print(a)

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    print('pass')
else:
    print("카드를 꺼내라")

pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")
