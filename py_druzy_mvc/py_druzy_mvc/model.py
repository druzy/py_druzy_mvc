#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 21 déc. 2015

@author: druzy
'''

class Model(object):
    '''
    a Model of mvc
    '''


    def __init__(self):
        '''
        Constructor
        '''
        object.__init__(self)
        
        self._listeners=list()
    
    def add_property_change_listener(self,listener):
        """
        add a listener to the model
        """
        self._listeners.append(listener)
        
    def remove_property_change_listener(self,listener):
        """
        remove a listener to the model
        """
        self._listeners.remove(listener)
        
    def fire_property_change(self,property_change_event):
        """
        déclenche un évènement
        """
        for listener in self._listeners:
            listener.property_change(property_change_event)
        