#coding=utf-8
#-*- coding: utf-8 -*-

'''
Created on Jul 30, 2014

@author: 
'''

a = 21
b = 10

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**2)
print(a%b)
print(a//b)

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

c = a + b
print(c)

c += a
print(c)

c -= a
print(c)

c *= a
print(c)

c /= a
print(c)

c = 2

c **= a
print(c)

c %= a
print(c)

c //= a
print(c)


d = 60
e = 13
f = 0

f = d & e
print(f)

f = d | e
print(f)

f = d ^ e
print(f)

f = ~ e
print(f)

f = e >> 2
print(f)

f = e << 2
print(f)

if True or True and False :
    print('true')
else :
    print('false')

m = 1
n = 2
if m and n :
    print('true')

if m-n :
    print('true')

if not m-1 :
    print('true')

l = [1,'2',3,'4',5]
k = 3
if k in l :
    print('k is available in the list')
else :
    print('k is not available in the list')

i = 10
j = 10
print(i is j)
j = 20
print(i is not j)

print(10 + 2 * 3)

if __name__ == '__main__' :
    pass