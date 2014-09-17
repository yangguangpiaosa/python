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
        actionmenu = tk.Menu(menubar,tearoff=0)
        actionmenu.add_command(label='Start',command=self.parent.menu_action_start)
        actionmenu.add_command(label='Restart',command=self.parent.menu_action_restart)
        actionmenu.add_separator()
        actionmenu.add_command(label='Quit',command=self.parent.menu_action_quit)
        menubar.add_cascade(label='Action',menu=actionmenu)
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