'''
Created on Dec 28, 2013

@author: Nick Crawford
'''

from graph.datastructs.Stack import Stack
from graph.graphs import Graph

__all__ = ['dfs', 'dfs_tree', 'dfs_postorder', 'dfs_preorder']

def dfs(graph, source=None):
    if source is None:
        source = graph[0]
    closed = set()
    open_ = Stack(source)
    while not open_.is_empty():
        u = open_.pop()
        closed.add(u)
        union = closed.union(open_)
        for v in graph.neighbors[u]:
            if v not in union:
                open_.push(v)
                yield u,v

def dfs_tree(graph, source=None):
    g = Graph()
    g.add_all(graph.nodes())
    g.add_edges(dfs(graph, source))
    return g
    
def dfs_preorder(graph, source=None):
    return
    
def dfs_postorder(graph, source=None):
    return