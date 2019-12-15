'''
Created on Mar 6, 2017

@author: MT
'''

class ZigzagIterator(object):
    def __init__(self, v1, v2):
        self.vec = [v1, v2]
        self.pointer = 0
    
    def next(self):
        while self.hashNext():
            if self.vec[self.pointer]:
                val = self.vec[self.pointer][0]
                self.vec[self.pointer].pop()
                self.pointer += 1
                if self.pointer >= len(self.vec):
                    self.pointer = 0
                return val
            else:
                self.pointer += 1
                if self.pointer >= len(self.vec):
                    self.pointer = 0
        return None
    
    def hasNext(self):
        return any([x != [] for x in self.vec])
