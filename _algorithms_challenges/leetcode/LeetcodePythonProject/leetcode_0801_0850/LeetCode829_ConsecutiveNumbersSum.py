'''
Created on May 6, 2018

@author: tongq
'''
class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = N
        res = 1
        i = 3
        while n%2 == 0:
            n /= 2
        while i*i <= n:
            count = 0
            while n%i == 0:
                n //= i
                count += 1
            res *= count+1
            i += 2
        return res if n == 1 else res*2
