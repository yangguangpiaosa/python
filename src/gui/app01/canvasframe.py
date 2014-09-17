# coding=utf-8
# -*- coding:utf-8 -*-

import tkinter as tk
import gui.app01.canvas

class canvasframe(tk.Frame):
    '''
    '''
    def __init__(self, master):
        '''
        '''
        tk.Frame.__init__(self, master)
        self.parent = master
        self.grid()
        self.speedControl = tk.Scale(self,orient=tk.HORIZONTAL, label="ball speed",
                           from_=-200, to=200,length=600)
        self.speedControl.grid()
        self.addCanvas()
        
    def addCanvas(self):
        '''
        '''
        self.crashball = gui.app01.canvas.mycanvas(self,width=598,height=398,background='#FFFFFF')

if __name__ == '__main__' :
    pass