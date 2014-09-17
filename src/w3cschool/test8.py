# coding=utf-8
# -*- coding:utf-8 -*-

import time

print(time.time())

print(time.time()/3600/24/365)

print(time.localtime(time.time()))

print(time.asctime(time.localtime(time.time())))

import calendar

print(calendar.month(2014,8))

print(calendar.isleap(2100))

print(time.strftime('%Y-%m-%d %X',time.localtime(time.time())))

def printstr(s):
    """print string"""
    print(s)

def test1(s1, *s2):
    print('------', s1)
    for v in s2:
        print('++++++',v)

sum1 = lambda x1,x2:x1+x2

if __name__ == '__main__' :
    printstr('aaaaaaa')
    test1(1,2,3,4,5)
    print(sum1(1,2))
    print(sum1('1','2'))
    