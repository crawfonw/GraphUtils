'''
Created on Dec 28, 2013

@author: Nick Crawford
'''

from graph.datastructs.Stack import Stack

__all__ = ['dfs', 'dfs_tree']

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

def dfs_tree(graph, source):
    return
    
def dfs_preorder(graph, source):
    return
    
def dfs_postorder(graph, source):
    return