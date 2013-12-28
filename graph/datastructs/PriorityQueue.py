'''
Created on Dec 28, 2013

@author: Nick Crawford
'''
import Queue
import heapq

class PriorityQueue(Queue.Queue):
    
    def __init__(self, initial_set):
        super(PriorityQueue, self).__init__(initial_set)
        
    def enqueue(self, obj, priority):
        heapq.heappush(self.objs, (priority, obj))
        
    def dequeue(self):
        (priority,item) = heapq.heappop(self.objs)
        return item
