# coding=utf-8
# -*- coding:utf-8 -*-

import threading
import time

class Mythread(threading.Thread):
    counter = 0
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
    
    def run(self):
        while Mythread.counter < 10:
            time.sleep(2)
            print(self.name,Mythread.counter)
            Mythread.counter += 1

if __name__ == '__main__' :
    t1 = Mythread('thread-1')
    t2 = Mythread('thread-2')
    t1.start()
    t2.start()