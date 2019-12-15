'''
Created on Apr 20, 2018

@author: tongq
'''
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        outdegrees = [0]*n
        inlinks = [[] for i in range(n)]
        for i in range(n):
            outdegrees[i] = len(graph[i])
        for i in range(n):
            for j in graph[i]:
                inlinks[j].append(i)
        queue = []
        for i in range(n):
            if outdegrees[i] == 0:
                queue.append(i)
        res = []
        while queue:
            i = queue.pop(0)
            res.append(i)
            for j in inlinks[i]:
                outdegrees[j] -= 1
                if outdegrees[j] == 0:
                    queue.append(j)
        res.sort()
        return res
    
    def eventualSafeNodes_own_TLE(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        isCycle = [False]*n
        for i in range(n):
            visited = set()
            self.getIsCycle(i, i, graph, visited, isCycle)
        return [i for i in range(n) if not isCycle[i]]
    
    def getIsCycle(self, i, start, graph, visited, isCycle):
        if start in visited or isCycle[start]:
            isCycle[i] = True
            return
        visited.add(start)
        for nextVal in graph[start]:
            self.getIsCycle(i, nextVal, graph, visited, isCycle)
        visited.remove(start)
    
    def test(self):
        testCases = [
            [[1,2],[2,3],[5],[0],[5],[],[]],
            [[],[0,2,3,4],[3],[4],[]],
        ]
        for graph in testCases:
            print('graph: %s' % graph)
            result = self.eventualSafeNodes(graph)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
