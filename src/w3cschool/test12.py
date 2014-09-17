# coding=utf-8
# -*- coding:utf-8 -*-

import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) (.*)', line, re.M|re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
    print("matchObj.group(3) : ", matchObj.group(3))
    print(matchObj.groups())
else:
    print("No match!!")

teststr = 'python test'
match = re.search('[Pp]ython',teststr)
print(match.group())

replace = 'pythonjavapython'
sub = re.sub('java','python',replace)
print(sub)

if __name__ == '__main__' :
    pass