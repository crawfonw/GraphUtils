'''
Created on Dec 28, 2013

@author: Nick Crawford
'''

import Container

class Queue(Container.Container):
    '''
    classdocs
    '''

    def __init__(self, initial_set):
        super(Queue, self).__init__(initial_set)
        
    def enqueue(self, obj):
        self.objs.insert(0, obj)
    
    def dequeue(self):
        return self.objs.pop()
    
    def is_empty(self):
        return len(self.objs) == 0
    
    def add(self, obj):
        self.enqueue(obj)
    
    def get_next(self):
        return self.dequeue()