'''
Created on Dec 28, 2013

@author: Nick Crawford
'''

class Container(object):
    '''
    classdocs
    '''

    def __init__(self, initial_set=[]):
        '''
        Constructor
        '''
        self.objs = initial_set
        
    def __repr__(self):
        return '%s(initial_set=%s)' % (self.__class__.__name__, self.objs)
    
    def __str__(self):
        return self.objs
    
    def __iter__(self):
        return iter(self.objs)

    def add(self, obj):
        raise NotImplementedError()
        
    def get_next(self):
        raise NotImplementedError()