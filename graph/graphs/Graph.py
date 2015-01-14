'''
Created on Dec 27, 2013

@author: Nick Crawford
'''

class Graph(object):
    '''
    classdocs
    '''

    def __init__(self, nodes=[], directed=True):
        '''
        Constructor
        '''
        self.directed = directed
        self.neighbors = {}
        self.edge_weights = {}
        for node in nodes:
            self.neighbors[node] = set()
        self.size = len(nodes)
        self.edges = 0
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, key):
        return self.neighbors.keys()[key]
    
    def __iter__(self):
        return iter(self.neighbors.keys())
    
    def __repr__(self):
        return '%s(nodes=%s, directed=%s)' % (self.__class__.__name__, self.size, self.directed)
    
    def __str__(self):
        return '%s, %s' % (self.neighbors.keys(), self.edge_weights)
    
    def adjacent(self, node1, node2):
        return node2 in self.neighbors(node1)
    
    def neighbors(self, node):
        return self.neighbors.get(node)
    
    def add_all(self, nodes):
        for node in nodes:
            self.neighbors[node] = set()
            self.size += 1
        
    def add_node(self, node, edges=[], weights=[]):
        self.neighbors[node] = set(edges)
        self.size += 1
        self.edges += len(edges)
        if len(edges) != len(weights):
            weights = [1]*len(edges)
        for i, edge in enumerate(edges):
            self.edge_weights[(node,edge)] = weights[i]
            if not self.directed:
                self.edge_weights[(edge,node)] = weights[i]
    
    def add_edge(self, from_node, to_node, weight=1):
        if from_node not in self.nodes():
            self.add_node(from_node)
        if to_node not in self.nodes():
            self.add_node(to_node)
        if to_node not in self.neighbors[from_node] and from_node not in self.neighbors[to_node]:
            self.neighbors[from_node].add(to_node)
            self.edge_weights[(from_node, to_node)] = weight
            if from_node != to_node and not self.directed:
                self.neighbors[to_node].add(from_node)
                self.edge_weights[(to_node, from_node)] = weight
            self.edges += 1
        else:
            raise ValueError('Edge already exists between %s and %s.' % (from_node, to_node))
    
    def add_edges(self, edge_list):
        for edge in edge_list:
            if len(edge) == 2:
                u,v = edge
                w = 1
            elif len(edge) == 3:
                u,v,w = edge
            else:
                raise ValueError('Edge tuple of length %s is not supported.' % str(len(edge)))
            self.add_edge(u, v, w)
    
    def delete_edge(self, from_node, to_node):
        self.neighbors[from_node].remove(to_node)
        del self.edge_weights[(from_node, to_node)]
        if from_node != to_node and not self.directed:
            self.neighbors[from_node].remove(to_node)
            del self.edge_weights[(to_node, from_node)]
        self.edges -= 1
    
    def nodes(self):
        return self.neighbors.keys()
    
    def delete_node(self, node):
        for neighbor in self.neighbors[node]:
            self.delete_edge(node, neighbor)
        for edge in self.edge_weights.keys():
            if node in edge:
                del self.edge_weights[edge]
        del self.neighbors[node]
        self.size -= 1
    
    def get_edge_weight(self, from_node, to_node):
        return self.edge_weights[(from_node, to_node)]
    
    def set_edge_weight(self, from_node, to_node, weight):
        self.edge_weights[(from_node, to_node)] = weight
        if not self.directed:
            self.edge_weights[(to_node, from_node)] = weight