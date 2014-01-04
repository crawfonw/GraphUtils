'''
Created on Dec 28, 2013

@author: Nick Crawford
'''

__all__ = ['implicit_graph_search']

parents = {}
closed = set()
open_ = set() 

def path(u, source, parents):
    path = []
    while parents[u] != source:
        path.insert(0, u)
        u = parents[u]
    return path

def implicit_expand(u, graph):
    return graph.neighbors[u]

def implicit_improve(u,v,w):
    union = closed.union(open_)
    if v not in union:
        open_.add(v)
        parents[v] = u

def implicit_graph_search(graph, source, target, container, expand, improve, weight):
    open_ = container(source)
    while not open_.is_empty():
        u = open_.get_next() #dictated by the data structure used; must remove item from container
        closed.add(u)
        if u == target:
            return path(u, source, parents)
        else:
            for v in expand(u):
                improve(u,v,weight)
    return None