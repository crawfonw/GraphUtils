'''
Created on Dec 28, 2013

@author: Nick Crawford
'''

__all__ = ['implicit_graph_search']

def path(u, source, parents):
    path = []
    while parents[u] != source:
        path.insert(0, u)
        u = parents[u]
    return path

def expand(u, graph):
    return graph.neighbors[u]

def implicit_graph_search(graph, source, target, data_container):
    parents = {}
    closed = set()
    open_ = data_container(source)
    while not open_.is_empty():
        u = open_.get_next() #dictated by the data structure used; must remove item from container
        closed.add(u)
        if u == target:
            return path(u, source, parents)
        else:
            union = closed.union(open_)
            for v in expand(u):
                if v not in union:
                    open_.add(v)
                    parents[v] = u
    return None