# coding=utf-8
# -*- coding:utf-8 -*-

import time
import _thread

def thread_method(name,delay):
    count = 0
    print(count)
    while count < 5 :
        print('dddd')
        time.sleep(delay)
        count += 1
        print(count)
        print('%s - %s' % (name,time.ctime(time.time())))

try:
    _thread.start_new_thread(thread_method,('Thread-1',2))
    _thread.start_new_thread(thread_method,('Thread-2',4))
except Exception as e:
    print(str(e))

if __name__ == '__main__' :
    pass