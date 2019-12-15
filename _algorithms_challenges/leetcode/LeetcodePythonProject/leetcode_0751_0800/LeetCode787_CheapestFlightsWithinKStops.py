'''
Created on Apr 12, 2018

@author: tongq
'''
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        import heapq
        graph = {}
        for f in flights:
            if f[0] not in graph:
                graph[f[0]] = [[f[2], f[1]]]
            else:
                graph[f[0]].append([f[2], f[1]])
        pq = [[0, K+1, src]]
        while pq:
            size = len(pq)
            for _ in range(size):
                curLen, level, node = heapq.heappop(pq)
                if node == dst:
                    return curLen
                if level > 0:
                    for dist, node0 in graph.get(node, []):
                        heapq.heappush(pq, [curLen+dist, level-1, node0])
        return -1
    
    def test(self):
        testCases = [
            [3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1],
            [3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0],
            [4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1],
            [4, [[0,3,59],[2,0,83],[2,3,32],[0,2,97],[3,1,16],[1,3,16]], 3, 0, 3],
            [5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], 0, 2, 2],
        ]
        for n, flights, src, dst, k in testCases:
            result = self.findCheapestPrice(n, flights, src, dst, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
