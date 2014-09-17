# coding=utf-8
# -*- coding:utf-8 -*-

import tkinter as tk
import gui.app01.menu as mu
import gui.app01.canvasframe as ca

class simpleapp:
    '''
    A simple Application.
    '''
    def __init__(self, title='SimpleApp'):
        '''
        Init.
        '''
        self.win = tk.Tk()
        self.win.title(title)
        self.win.geometry('600x500')
        
        #menu options
        self.win.menu_action_start = self.menu_action_start
        self.win.menu_action_restart = self.menu_action_restart
        self.win.menu_action_quit = self.menu_action_quit
        self.win.menu_help_about = self.menu_help_about
        
        #init menu
        mu.menu(self.win)
        
        #init canvas
        ca.canvasframe(self.win)
        self.win.mainloop()
    
    def menu_action_start(self):
        print('start...')
    
    def menu_action_restart(self):
        print('restart...')
    
    def menu_action_quit(self):
        self.win.quit()
    
    def menu_help_about(self):
        print('about...')

if __name__ == '__main__' :
    app = simpleapp('Crash Ball')
    