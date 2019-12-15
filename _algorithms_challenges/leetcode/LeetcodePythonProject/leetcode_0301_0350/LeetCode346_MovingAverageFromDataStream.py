'''
Created on Mar 21, 2017

@author: MT
'''

class MovingAverage(object):
    def __init__(self, size):
        self.size = size
        self.queue = []
    
    def next(self, val):
        if self.size <= 0: return 0
        if len(self.queue) == self.size:
            self.queue.pop(0)
        self.queue.append(val)
        return float(sum(self.queue))/len(self.queue)