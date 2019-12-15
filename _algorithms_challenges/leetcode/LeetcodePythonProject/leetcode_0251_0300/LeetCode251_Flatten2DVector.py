'''
Created on Mar 1, 2017

@author: MT
'''

class Vector2D(object):
    def __init__(self, vec2d):
        self.values = [row for row in vec2d if row]
        self.row = 0
        self.col = 0
    
    def next(self):
        val = self.values[self.row][self.col]
        if self.col == len(self.values[self.row])-1:
            self.row += 1
            self.col = 0
        else:
            self.col += 1
        return val
    
    def hasNext(self):
        if self.row>=len(self.values):
            return False
        elif self.row < len(self.values)-1:
            return True
        else:
            if self.col < len(self.values[self.row]):
                return True
            else:
                return False
        