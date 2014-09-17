# coding=utf-8
# -*- coding:utf-8 -*-

import tkinter as tk
import time

class mycanvas(tk.Canvas):
    '''
    '''
    def __init__(self, master, **cnf):
        '''
        '''
        tk.Canvas.__init__(self, master, cnf)
        self.parent = master
        self.grid()
        self.initStatus()
        
    def initStatus(self):
        '''
        '''
        self.balls = []
        self.balls.append(ball(50,50,110,110,3,1,'red'))
        self.balls.append(ball(150,50,210,110,1,3,'green'))
        self.balls.append(ball(150,150,210,210,-2,2,'gray'))
        self.balls.append(ball(250,50,310,110,2,2,'black'))
        self.balls.append(ball(250,150,310,210,-2,2,'brown'))
        self.movings = []
        for i in range(len(self.balls)) :
            b = self.balls[i]
            self.movings.append(self.create_oval(b.x1,b.y1,b.x2,b.y2,fill=b.color))
        self.grid()
        self.moveBall()
    
    def moveBall(self):
        self.chekCrash()
        for i in range(len(self.balls)) :
            b = self.balls[i]
            #碰撞检测
            #if(b.ox <= b.r or b.ox >= 600-b.r) :
            #    b.vx = -1.0 * b.vx
            #if(b.oy <= b.r or b.oy >= 400-b.r) :
            #    b.vy = -1.0 * b.vy
            rate = self.parent.speedControl.get() * 0.015
            self.move(self.movings[i],b.vx * rate,b.vy * rate)
            b.updatePos(b.x1+b.vx * rate,b.y1+b.vy * rate,b.x2+b.vx * rate,b.y2+b.vy * rate,b.vx,b.vy)
        self.after(10, self.moveBall)
    
    def chekCrash(self):
        for i in range(len(self.balls)) :
            b = self.balls[i]
            #碰撞检测
            #碰壁
            if(b.ox <= b.r or b.ox >= 600-b.r) :
                b.vx = -1.0 * b.vx
            if(b.oy <= b.r or b.oy >= 400-b.r) :
                b.vy = -1.0 * b.vy
            #两球相撞
            if(b.crashed == False) :
                for j in range(len(self.balls)) :
                    if j != i :
                        if((self.balls[j].ox-b.ox)**2+(self.balls[j].oy-b.oy)**2 <= (self.balls[j].r+b.r)**2) :
                            b.crashed = True
                            self.balls[j].crashed = True
                            tempVx = b.vx
                            tempVy = b.vy
                            b.vx = self.balls[j].vx
                            b.vy = self.balls[j].vy
                            self.balls[j].vx = tempVx
                            self.balls[j].vy = tempVy
                            print(b.color,'ball crashed with',self.balls[j].color,'ball at:',time.strftime('%Y-%m-%d %X',time.localtime(time.time())))

class ball:
    '''
    '''
    def __init__(self,x1,y1,x2,y2,vx,vy,color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.vx = vx
        self.vy = vy
        self.color = color
        self.ox = round((x1+x2)/2,1)
        self.oy = round((y1+y2)/2,1)
        self.r = round(abs(x1-x2)/2,1)
        self.crashed = False
    
    def updatePos(self,x1,y1,x2,y2,vx,vy):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.vx = vx
        self.vy = vy
        self.ox = round((x1+x2)/2,1)
        self.oy = round((y1+y2)/2,1)
        self.r = round(abs(x1-x2)/2,1)
        self.crashed = False

if __name__ == '__main__' :
    pass