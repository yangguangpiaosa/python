#coding=utf-8
#-*- coding : utf-8 -*-

count = 0
while(count < 10) :
    if count % 2 ==0 :
        count += 1
        continue;
    print('Current value is', count)
    count += 1;

count = 0
while True :
    if count > 10 :
        break
    print('value is', count)
    count += 1;

limit = input('Please input a number:')
limit = int(limit)
factors = []
n = 1
while n <= limit :
    if limit % n == 0 :
        factors.append(n);
    n += 1;
else :
    print('loop end.')
print('factors are:', factors)

ll = '123456'
for letter in ll :
    print(letter)
else :
    print('loop end.')

fruits = ['apple','pear','banana']
for i in range(len(fruits)) :
    print(fruits[i])

for m in range(2,100) :
    flag = True
    for n in range(2,m-1) :
        if m % n == 0 :
            flag = False
            break
    if flag :
        print(m,'是质数')

if __name__ == '__main__' :
    pass
