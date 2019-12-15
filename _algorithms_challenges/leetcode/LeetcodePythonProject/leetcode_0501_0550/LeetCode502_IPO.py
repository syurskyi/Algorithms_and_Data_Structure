'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        import heapq
        heapCap = []
        heapPro = []
        for c, p in zip(Capital, Profits):
            heapq.heappush(heapCap, (c, p))
        for _ in range(k):
            while heapCap and heapCap[0][0] <= W:
                c, p = heapq.heappop(heapCap)
                heapq.heappush(heapPro, (-p, c))
            if not heapPro:
                break
            p, c = heapq.heappop(heapPro)
            W += -p
        return W
