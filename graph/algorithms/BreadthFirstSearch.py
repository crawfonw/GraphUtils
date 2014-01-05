'''
Created on Jan 5, 2014

@author: Nick Crawford
'''

from graph.datastructs.Queue import Queue
from graph.graphs import Graph

__all__ = ['bfs', 'bfs_tree', 'bfs_postorder', 'bfs_preorder']

def bfs(graph, source=None):
    if source is None:
        source = graph[0]
    closed = set()
    open_ = Queue(source)
    while not open_.is_empty():
        u = open_.dequeue()
        closed.add(u)
        union = closed.union(open_)
        for v in graph.neighbors[u]:
            if v not in union:
                open_.enqueue(v)
                yield u,v

def bfs_tree(graph, source=None):
    g = Graph()
    g.add_all(graph.nodes())
    g.add_edges(bfs(graph, source))
    return g
    
def bfs_preorder(graph, source=None):
    return
    
def bfs_postorder(graph, source=None):
    return