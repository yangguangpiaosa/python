# coding=utf-8
# -*- coding:utf-8 -*-

import tkinter as tk

class about(tk.Frame):
    def __int__(self, master):
        print('dddfffdddfff')
        tk.Frame.__init__(self, master);
        self.parent = master
        self.grid()
        print('aaaaa.....')
        self.showInfo()
    
    def showInfo(self):
        print('help...')
        canvas = tk.Canvas(self)
        canvas.create_text(20, 30, anchor=tk.W, font="Purisa",
            text="Most relationships seem so transitory")
        canvas.create_text(20, 60, anchor=tk.W, font="Purisa",
            text="They're good but not the permanent one")
        canvas.create_text(20, 130, anchor=tk.W, font="Purisa",
            text="Who doesn't long for someone to hold")
        canvas.create_text(20, 160, anchor=tk.W, font="Purisa",
            text="Who knows how to love without being told")                   
        canvas.create_text(20, 190, anchor=tk.W, font="Purisa",
            text="Somebody tell me why I'm on my own")            
        canvas.create_text(20, 220, anchor=tk.W, font="Purisa",
            text="If there's a soulmate for everyone")               
        canvas.grid()