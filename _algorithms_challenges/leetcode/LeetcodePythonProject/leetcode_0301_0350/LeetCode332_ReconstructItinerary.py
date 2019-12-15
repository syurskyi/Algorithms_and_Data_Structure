'''
Created on Mar 19, 2017

@author: MT
'''

import heapq

class Solution(object):
    def findItinerary_orig(self, tickets):
        if not tickets:
            return []
        hashmap = {}
        for t1, t2 in tickets:
            if t1 not in hashmap:
                hashmap[t1] = []
            heapq.heappush(hashmap[t1], t2)
        result = []
        self.dfs(result, hashmap, 'JFK')
        return result
        
    def dfs(self, result, hashmap, elem):
        while hashmap.get(elem):
            self.dfs(result, hashmap, heapq.heappop(hashmap[elem]))
        result.insert(0, elem)
    
    def test(self):
        testCases = [
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
            [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
            [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]],
        ]
        for tickets in testCases:
            print('tickets: %s' % tickets)
            result = self.findItinerary(tickets)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

