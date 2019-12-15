'''
Created on Feb 23, 2017

@author: MT
'''
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        q, x, res = n, 1, 0
        while q > 0:
            digit = q%10
            q //= 10
            res += q*x
            if digit == 1:
                res += n%x+1
            elif digit > 1:
                res += x
            x *= 10
        return res
