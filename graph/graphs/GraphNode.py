'''
Created on Dec 27, 2013

@author: Nick Crawford
'''

class GraphNode(object):
    '''
    classdocs
    '''

    def __init__(self, label, data):
        '''
        Constructor
        '''
        self.label = label
        self.data = data
        
    def __str__(self):
        return self.label
    
    def __repr__(self):
        return '%s(label=%s,data=%s)' % (self.__class__.__name__, self.label, self.data)