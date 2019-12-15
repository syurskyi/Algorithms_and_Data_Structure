'''
Created on Apr 1, 2017

@author: MT
'''

class RandomizedSet(object):
    def __init__(self):
        self.nums = []
        self.pos = {}
    
    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums)-1
            return True
        else:
            return False
    
    def remove(self, val):
        if val in self.pos:
            ind = self.pos[val]
            lastVal = self.nums[-1]
            self.nums[ind] = lastVal
            self.pos[lastVal] = ind
            del self.pos[val]
            self.nums.pop()
            return True
        return False
    
    def getRandom(self):
        import random
        return random.choice(self.nums)
