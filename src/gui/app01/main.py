# coding=utf-8
# -*- coding:utf-8 -*-

import tkinter as tk

class simpleapp:
    '''
    simple app.
    '''
    def __init__(self,title='simple app'):
        '''
        init.
        '''
        self.win = tk.Tk()
        self.win.title(title)
        self.win.geometry('600x400')
        self.addMenu()
        self.addCanvas()
        self.win.mainloop()
    
    def addMenu(self):
        '''
        add menu.
        '''
        menubar = tk.Menu(self.win)
        #action menu
        actionmenu = tk.Menu(menubar,tearoff=0)
        actionmenu.add_command(label='Start',command=None)
        actionmenu.add_command(label='Restart',command=None)
        actionmenu.add_separator()
        actionmenu.add_command(label='Quit',command=self.win.quit)
        menubar.add_cascade(label='Action',menu=actionmenu)
        #help menu
        helpmenu = tk.Menu(menubar,tearoff=0)
        helpmenu.add_command(label='About',command=None)
        menubar.add_cascade(label='Help',menu=helpmenu)
        
        self.win.config(menu=menubar)
        
    def addCanvas(self):
        '''
        add canvas
        '''
        self.canvas = tk.Canvas(self.win,width=598,height=398,background='#FFFFFF')
        self.ball = self.canvas.create_oval("0.60i", "0.60i", "1.60i", "1.60i", fill="green")
        self.win.after(10, self.moveBall)
        self.canvas.grid()
    
    def moveBall(self):
        '''
        move balls.
        '''
        self.canvas.move(self.ball,0.5,0.5)
        self.win.after(10, self.moveBall)

if __name__ == '__main__' :
    app = simpleapp('simple app')