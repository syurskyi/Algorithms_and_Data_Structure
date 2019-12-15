'''
Created on Jun 10, 2018

@author: tongq
'''
class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        for i in range(N):
            graph[i] = set()
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        res = [0]*N
        count = [0]*N
        self.dfs(0, set(), graph, res, count)
        self.dfs2(0, set(), graph, res, count, N)
        return res
    
    def dfs(self, root, visited, graph, res, count):
        visited.add(root)
        for i in graph[root]:
            if i not in visited:
                self.dfs(i, visited, graph, res, count)
                count[root] += count[i]
                res[root] += res[i]+count[i]
        count[root] += 1
    
    def dfs2(self, root, visited, graph, res, count, N):
        visited.add(root)
        for i in graph[root]:
            if i not in visited:
                res[i] = res[root] - count[i] + N - count[i]
                self.dfs2(i, visited, graph, res, count, N)
    
    ##########################################################
    ######################## OWN TLE #########################
    ##########################################################
    def sumOfDistancesInTree_own_TLE(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = N
        graph = {}
        for i in range(n):
            graph[i] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        res = []
        for i in range(n):
            res.append(self.bfs(graph, i))
        return res
    
    def bfs(self, graph, i):
        res = 0
        queue = [i]
        visited = set([i])
        level = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                for node0 in graph[node]:
                    if node0 not in visited:
                        res += level
                        visited.add(node0)
                        queue.append(node0)
            level += 1
        return res
    
    def test(self):
        testCases = [
            [
                6,
                [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]],
            ],
        ]
        for n, edges in testCases:
            print('n: %s' % n)
            print('edges: %s' % edges)
            result = self.sumOfDistancesInTree(n, edges)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
