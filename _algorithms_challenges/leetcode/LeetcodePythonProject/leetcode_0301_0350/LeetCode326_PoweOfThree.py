'''
Created on Mar 18, 2017

@author: MT
'''

class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0: return False
        return (3**19)%n == 0
    
    def isPowerOfThreeMath(self, n):
        if n <= 0: return False
        while n > 1:
            if n % 3 != 0:
                return False
            n = n/3
        return True
