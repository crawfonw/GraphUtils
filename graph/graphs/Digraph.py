'''
Created on Dec 27, 2013

@author: Nick Crawford
'''

import Graph

class Digraph(Graph.Graph):
    
    def __init__(self):
        super(Digraph, self).__init__()
        
    def add_edge(self, from_node, to_node, weight=1):
        if to_node not in self.neighbors[from_node]:
            self.neighbors[from_node].add(to_node)
            self.edge_weights[(from_node, to_node)] = weight
            self.nodes += 1
        else:
            raise ValueError('Edge already exists between %s and %s.' % (from_node, to_node))
    
    def delete_edge(self, from_node, to_node):
        self.neighbors[from_node].remove(to_node)
        del self.edge_weights[(from_node, to_node)]
        self.edges -= 1
    
    def add_node_with_edges(self, node, edges=[], weights=[]):
        self.neighbors[node] = set(edges)
        self.nodes += 1
        self.edges += len(edges)
        if len(edges) != len(weights):
            weights = [1]*len(edges)
        for i, edge in enumerate(edges):
            self.edge_weights[(node,edge)] = weights[i]
    
    def set_edge_weight(self, from_node, to_node, weight):
        self.edge_weights[(from_node, to_node)] = weight