'''
Created on May 12, 2018

@author: tongq
'''
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    import random
    return random(0, 1) == 0

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n-1
        while l < r:
            if knows(l, r):
                l += 1
            else:
                r -= 1
        for i in range(n):
            if i == l or (knows(i, l) and not knows(l, i)):
                continue
            else:
                return -1
        return l
