'''
Created on Oct 3, 2019

@author: tongq
'''
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        import heapq
        h = []
        res = i = 0
        cur = startFuel
        while cur < target:
            while i < len(stations) and stations[i][0] <= cur:
                heapq.heappush(h, -stations[i][1])
                i += 1
            if not h:
                return -1
            cur += -heapq.heappop(h)
            res += 1
        return res
