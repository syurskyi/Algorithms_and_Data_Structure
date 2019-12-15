'''
Created on May 31, 2018

@author: tongq
'''
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0: return [n]
        res = self.grayCode(n-1)
        toAdd = 1 << (n-1)
        for i in range(len(res)-1, -1, -1):
            res.append(toAdd+res[i])
        return res
