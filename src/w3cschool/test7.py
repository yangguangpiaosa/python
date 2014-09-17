# coding=utf-8
# -*- coding:utf-8 -*-

import math,random

a = int('101',2)
print(a)

b = float('101.01')
print(b)

c = ord('A')
print(c)

s1 = abs(-5)
print(s1)

s2 = math.ceil(4.4)
print(s2)

s3 = math.ceil(-4.4)
print(s3)

print(max(2,9,4,5,1))

print(pow(2,3))

print(round(math.sqrt(3),2))

for i in range(10) :
    print("======",random.choice(range(10)))

print(random.random())

print(random.uniform(1,8))

lst = [1,2,3,4,5,6,7,8,9,0]
print("before:",lst)
random.shuffle(lst)
print("after:",lst)

print(math.sin(math.pi/6))

print(math.e)

print(math.pi)

print('format %(str)s' % {'str':'aaa'})

hi = '''hi
all'''

print(hi)

print(tuple('12345'))

d1 = dict(one=1,
          two=2)
d2 = dict(three=3,
          four=4)
d1.update(d2)
print(d1)
print(d1.keys())

if __name__ == '__main__' :
    pass
