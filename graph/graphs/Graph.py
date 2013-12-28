'''
Created on Dec 27, 2013

@author: Nick Crawford
'''

class Graph(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.nodes = 0
        self.edges = 0
        self.neighbors = {}
        self.edge_weights = {}
        
    def __str__(self):
        return (self.nodes(), self.edges())
    
    def __repr__(self):
        return '%s(*args)' % (self.__class__.__name__)
    
    def __len__(self):
        return self.nodes
    
    def add_all(self, nodes):
        for node in nodes:
            self.neighbors[node] = set()
            self.nodes += 1
        
    def add_node_with_edges(self, node, edges=[], weights=[]):
        self.neighbors[node] = set(edges)
        self.nodes += 1
        self.edges += len(edges)
        if len(edges) != len(weights):
            weights = [1]*len(edges)
        for i, edge in enumerate(edges):
            self.edge_weights[(node,edge)] = weights[i]
            self.edge_weights[(edge,node)] = weights[i]
    
    def adjacent(self, node1, node2):
        return node2 in self.neighbors(node1)
    
    def neighbors(self, node):
        return self.neighbors.get(node)
    
    def add_edge(self, from_node, to_node, weight=1):
        if to_node not in self.neighbors[from_node] and from_node not in self.neighbors[to_node]:
            self.neighbors[from_node].add(to_node)
            self.edge_weights[(from_node, to_node)] = weight
            if from_node != to_node:
                self.neighbors[to_node].add(from_node)
                self.edge_weights[(to_node, from_node)] = weight
            self.edges += 1
        else:
            raise ValueError('Edge already exists between %s and %s.' % (from_node, to_node))
    
    def delete_edge(self, from_node, to_node):
        self.neighbors[from_node].remove(to_node)
        del self.edge_weights[(from_node, to_node)]
        if from_node != to_node:
            self.neighbors[from_node].remove(to_node)
            del self.edge_weights[(to_node, from_node)]
        self.edges -= 1
    
    def nodes(self, node):
        return self.neighbors.keys()
    
    def delete_node(self, node):
        for neighbor in self.neighbors[node]:
            self.delete_edge(node, neighbor)
        for edge in self.edge_weights.keys():
            if node in edge:
                del self.edge_weights[edge]
        del self.neighbors[node]
        self.nodes -= 1
    
    def get_edge_weight(self, from_node, to_node):
        return self.edge_weights[(from_node, to_node)]
    
    def set_edge_weight(self, from_node, to_node, weight):
        self.edge_weights[(from_node, to_node)] = weight
        self.edge_weights[(to_node, from_node)] = weight