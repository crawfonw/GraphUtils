'''
Created on Dec 28, 2013

@author: Nick Crawford
'''

from ImplicitGraphSearch import implicit_graph_search
from graph.datastructs.Stack import Stack

__all__ = ['dfs', 'dfs_tree']

def dfs(graph, source=None, target):
    if source is None:
        source = graph[0]
    return implicit_graph_search(graph, source, target, Stack())

def dfs_tree(graph, source):
    return
    
def dfs_preorder(graph, source):
    return
    
def dfs_postorder(graph, source):
    return