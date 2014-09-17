# coding=utf-8
# -*- coding:utf-8 -*-

import tkinter as tk
class menu(tk.Frame):
    '''
    menu part.
    '''
    def __init__(self,master):
        '''
        init.
        '''
        tk.Frame.__init__(self, master)
        self.parent = master
        self.grid()
        self.addButton()
    
    def addButton(self):
        '''
        add menu.
        '''
        menubar = tk.Menu(self)
        #action menu
        optionsmenu = tk.Menu(menubar,tearoff=0)
        optionsmenu.add_command(label='Calculator',command=self.parent.menu_options_calculator)
        optionsmenu.add_separator()
        optionsmenu.add_command(label='Exit',command=self.parent.menu_options_quit)
        menubar.add_cascade(label='Options',menu=optionsmenu)
        #help menu
        helpmenu = tk.Menu(menubar,tearoff=0)
        helpmenu.add_command(label='About',command=self.parent.menu_help_about)
        menubar.add_cascade(label='Help',menu=helpmenu)
        
        self.parent.config(menu=menubar)

if __name__ == '__main__' :
    root = tk.Tk()
    root.geometry('600x400')
    menu = menu(root)
    root.title('Simple Application')
    root.mainloop()