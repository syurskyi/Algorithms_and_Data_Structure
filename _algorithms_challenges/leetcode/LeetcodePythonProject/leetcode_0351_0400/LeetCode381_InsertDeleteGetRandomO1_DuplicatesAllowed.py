'''
Created on Apr 1, 2017

@author: MT
'''

class RandomizedCollection(object):
    def __init__(self):
        self.vals = []
        self.pos = {}
    
    def insert(self, val):
        self.vals.append(val)
        if val in self.pos:
            self.pos[val].add(len(self.vals)-1)
            return False
        else:
            self.pos[val] = set([len(self.vals)-1])
            return True
    
    def remove(self, val):
        if val in self.pos:
            lastVal = self.vals[-1]
            ind = self.pos[val].pop()
            self.vals[ind] = lastVal
            if self.pos[lastVal]:
                self.pos[lastVal].add(ind)
                self.pos[lastVal].discard(len(self.vals)-1)
            self.vals.pop()
            if not self.pos[val]:
                del self.pos[val]
            return True
        return False
    
    def getRandom(self):
        import random
        return random.choice(self.vals)
    