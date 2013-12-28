'''
Created on Dec 27, 2013

@author: Nick Crawford
'''

import Graph

class Digraph(Graph.Graph):
    
    def __init__(self, nodes=[]):
        super(Digraph, self).__init__(nodes, True)