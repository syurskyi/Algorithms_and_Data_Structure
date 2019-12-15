'''
Created on Nov 8, 2017

@author: MT
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        sig = 1 if x >= 0 else -1
        x = abs(x)
        while x > 0:
            digit = x%10
            res = res*10 + digit
            x = (x-digit)//10
        res = res*sig
        if res > 2**31-1 or res < -2**31:
            return 0
        else:
            return res
