#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 21 déc. 2015

@author: druzy
'''

class PropertyChangeEvent:
    '''
    a explicite name for this class
    
    define by ;
    - the source
    - the name
    - the old value
    - the new value
    '''

    def __init__(self, source, property_name, old_value, new_value):
        '''
        Constructor
        '''
        self.source=source
        self.property_name=property_name
        self.old_value=old_value
        self.new_value=new_value
        
    