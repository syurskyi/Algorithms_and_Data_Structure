'''
Created on Sep 30, 2019

@author: tongq
'''
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = N
        i = 0
        prev = -1
        res = 0
        while n > 0:
            d = n % 2
            if d == 1:
                if prev >= 0:
                    res = max(res, i-prev)
                prev = i
            n //= 2
            i += 1
        return res
