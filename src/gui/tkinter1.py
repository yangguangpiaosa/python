# coding=utf-8
# -*- coding:utf-8 -*-

import tkinter as tk

class Application(tk.Frame):
    '''
    A simple GUI application.
    '''
    def __init__(self,master=None):
        '''
        init.
        '''
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        '''
        create widgets.
        '''
        self.quitButton = tk.Button(self,text='Quit',command=self.quit)
        self.quitButton.grid()

if __name__ == '__main__' :
    app = Application()
    app.master.title('Simple Application')
    app.mainloop()