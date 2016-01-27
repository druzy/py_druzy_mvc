#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 22 déc. 2015

@author: druzy
'''

from view import View

class Controller:
    '''
    a controller of MVC
    define by the view
    '''

    def __init__(self, model):
        '''
        Constructor
        '''
        self.model=model
        self._views=list()
        
    def add_view(self,view):
        """
        add a view to the controller
        """
        self._views.append(view)
        self.model.add_property_change_listener(view)
        
    def remove_view(self,view):
        """
        remove a view to the model
        """
        self._views.remove(view)
        self.model.remove_property_change_listener(view)
        
    def display_views(self):
        """
        display all the views of the controller
        """
        for view in self._views:
            view.display()
    
    def close_views(self):
        """
        close all the views of this Controller
        """
        for view in self._views:
            view.close()
            
    def views_on_top(self):
        """
        push the views on top
        """
        for view in self._views:
            view.on_top()
            
    def notify_action(self,view,action,**kwargs):
        """
        notify an action to the controller
        
        the  subclass must override this
        """
            
    