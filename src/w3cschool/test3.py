#coding=utf-8
#-*- coding: utf-8 -*-

'''
Created on Jul 28, 2014

@author: 
'''

a = b = c = 1
print(a)
print(b)
print(c)

a,b,c = 1,1,"something"
print(a)
print(b)
print(c)

#Python中的number
num = 10
print(num)
del num
#print(num)

#Python中的String
s = "helloworld"
print(s)
print(s[2])
print(s[1:5])
print(s[1:])
print(s[:6])
print(s * 3)
print(s[5:] * 2)

#Python中的List
first = [1,2,"3",4,5,[61,62]]
second = [7.0,8,9]
print(first)
print(second)
print(first[2:4])
print(second * 2)
print(first + second)

#Python中的元组
tuple1 = (1,2,3,'4',"5",6)
tuple2 = (7,8,9)
print(tuple1)
print(tuple1 + tuple2)
print(tuple1[1:3])

#Python中 元字典
dict1 = {3:'three'}
dict1[1] = "one";
dict1[2] = 2;
print(dict1)
print(dict1.keys())
print(dict1.values())

convert = int('101',2)
print(convert)

comp = complex(1,1)
print(comp.real)
print(comp.imag)

print(str(first)[2:6])

rep = 'adfsdfa' + 'dddddddd';
print(repr(rep))

evalstr = eval(repr(rep));
print(evalstr)

print(tuple('helloworld'))
print(list('helloworld'))
datas = set('helloworld')
print(datas)
print(datas.pop())
print(datas.pop())

datas1 = dict(one='1')
print(datas1)

print(frozenset('abcdefg'))

print(chr(65))

print(ord('A'))

print(hex(25))

print(oct(25))

if __name__ == '__main__' :
    pass