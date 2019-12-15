'''
Created on Mar 19, 2017

@author: MT
'''

class Solution(object):
    def isSelfCrossing(self, x):
        x = [0, 0, 0, 0]+x
        n = len(x)
        i = 4
        # outer spiral
        while i < n and x[i] > x[i-2]:
            i += 1
        if i == n:
            return False
        # check border
        if x[i] >= x[i-2]-x[i-4]:
            x[i-1] -= x[i-3]
        i += 1
        # inner spiral
        while i < n and x[i] < x[i-2]:
            i += 1
        return i != n
    
    def isSelfCrossing_another(self, x):
        if not x or len(x) < 3: return False
        for i in range(3, len(x)):
            if x[i] >= x[i-2] and x[i-3] >= x[i-1]:
                return True
            if i >= 4 and x[i]+x[i-4] >= x[i-2] and x[i-1] == x[i-3]:
                return True
            if i >= 5 and x[i-5]<=x[i-3] and x[i-4] <= x[i-2] and\
                x[i-1] <= x[i-3] and x[i-1]+x[i-4] >= x[i-3] and\
                x[i]+x[i-4] >= x[i-2] and x[i] <= x[i-2]:
                return True
        return False