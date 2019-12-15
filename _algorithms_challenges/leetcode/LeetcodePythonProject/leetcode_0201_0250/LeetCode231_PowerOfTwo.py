'''
Created on Feb 23, 2017

@author: MT
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        return bool(n&(n-1)==0)
    
    def isPowerOfTwoSlow(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        if n == 1: return True
        if n % 2 != 0:
            return False
        return self.isPowerOfTwo(n/2)