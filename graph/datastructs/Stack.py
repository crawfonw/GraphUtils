'''
Created on Dec 28, 2013

@author: Nick Crawford
'''

import Container

class Stack(Container.Container):
    
    def __init__(self, initial_set):
        super(Stack, self).__init__(initial_set)
        
    def push(self, obj):
        self.objs.append(obj)
        
    def pop(self):
        self.objs.pop()
        
    def is_empty(self):
        return len(self.objs) == 0
    
    def add(self, obj):
        self.push(obj)
    
    def get_next(self):
        return self.pop()