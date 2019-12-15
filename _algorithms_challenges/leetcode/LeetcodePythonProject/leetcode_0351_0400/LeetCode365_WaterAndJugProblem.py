'''
Created on Feb 27, 2018

@author: tongq
'''
class Solution(object):
    def canMeasureWater(self, x, y, z):
        if x+y<z: return False
        if x == z or y == z or x+y == z:
            return True
        while y != 0:
            tmp = y
            y = x%y
            x = tmp
        return bool(z%x==0)
