#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 22 déc. 2015

@author: druzy
'''

class View:
    '''
    a vue of MVC
    
    define by his controller
    '''


    def __init__(self,controller):
        '''
        Constructor
        '''
        self.controller=controller
        
    def display(self):
        """ Display the view 
        must be overrided"""
        pass
    
    def close(self):
        """ close the view
        must be overrided"""
        pass
    
    def is_displaying(self):
        """ return if the view is displaying
        must be overrided"""
        return True
    
    def on_top(self):
        """put on the top the view
        must be override
        """
        self.display()
        
    def property_change(self,property_change_event):
        """is called when a event is dispaching in the Model
        must be overrided"""
        pass
        