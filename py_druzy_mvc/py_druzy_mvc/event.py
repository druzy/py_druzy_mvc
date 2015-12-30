#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 21 déc. 2015

@author: druzy
'''

class PropertyChangeEvent(object):
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
        object.__init__(self)
        self.source=source
        self.property_name=property_name
        self.old_value=old_value
        self.new_value=new_value
        
class IndexedPropertyChangeEvent(PropertyChangeEvent):
    '''Evènement au sujet d'un changement sur un index
    
    define by ;
    - the source
    - the name
    - the old value
    - the new value
    - the index
    '''
    
    def __init__(self,source,property_name,old_value,new_value,index):
        PropertyChangeEvent.__init__(self, source, property_name, old_value, new_value)
        self.index=index
    
    
    