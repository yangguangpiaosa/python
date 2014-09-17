# coding=utf-8
# -*- coding:utf-8 -*-

i = input('please input something:')
print('You just inputted:', i)

f = open('test.txt', 'a+', encoding='utf-8')
f.write('aaa--test中文\r\n')
print(f.mode)
print(f.name)
f.close()
print(f.closed)

f2 = open('test.txt', 'r+', encoding='utf-8')
s2 = f2.read()
print(s2)
f2.close()

f3 = open('test.txt','r+',encoding='utf-8')
s3 = f3.read(10)
print('cursor move:',s3)
pos = f3.tell()
print('current position:',pos)
f3.seek(0,0)
pos = f3.tell()
print('now position:',pos)
f3.close()

testfile = open('test1.txt','a+',encoding='utf-8')
testfile.write('test file.')
testfile.close()

import os
os.renames('test1.txt', 'test2.txt')
os.remove('test2.txt')

os.mkdir('test')
os.rmdir('test')
print(os.getcwd())

if __name__ == '__main__' :
    pass