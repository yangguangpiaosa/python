# coding = utf-8
# -*- coding:utf-8 -*-

import tkinter as tk
import gui.app.menu as mu
import gui.app.helpinfo as helpinfo

'''
'''
class simple:
    '''
    A simple application.
    '''
    def __init__(self, title='SimpleApp'):
        '''
        Init.
        '''
        self.win = tk.Tk()
        self.win.title(title)
        self.win.geometry('600x500')
        
        #menu options
        self.win.menu_options_calculator = self.menu_options_calculator
        self.win.menu_options_quit = self.menu_options_quit
        self.win.menu_help_about = self.menu_help_about
        
        #init menu
        mu.menu(self.win)
        
        #init default child app
        helpinfo.about(self.win)
        
        self.win.mainloop()
    
    def menu_options_calculator(self):
        print('calculator...')
    
    def menu_options_quit(self):
        self.win.quit()
    
    def menu_help_about(self):
        print('ddddddd.........')
        helpinfo.about(self.win)

if __name__ == '__main__' :
    app = simple('SimpleApp V1.0')