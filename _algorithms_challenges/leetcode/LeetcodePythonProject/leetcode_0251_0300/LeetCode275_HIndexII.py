'''
Created on Mar 5, 2017

@author: MT
'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        count = [0]*(n+1)
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        res = 0
        sumVal = 0
        for i in range(n, -1, -1):
            sumVal += count[i]
            if sumVal >= i:
                return i
        return res
