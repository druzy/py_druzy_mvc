#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 22 déc. 2015

@author: druzy
'''

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
        self.views=list()
        