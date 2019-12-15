'''
Created on Mar 14, 2017

@author: MT
'''
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 0: return []
        if n == 1: return [0]
        graph = [set() for _ in range(n)]
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        leaves = []
        for i, nodes in enumerate(graph):
            if len(nodes) == 1:
                leaves.append(i)
        if not leaves:
            return []
        while n > 2:
            n = n-len(leaves)
            newLeaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    newLeaves.append(neighbor)
            leaves = newLeaves
        return leaves
    
    def test(self):
        testCases = [
            (4, [[1, 0], [1, 2], [1, 3]]),
            (6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]),
        ]
        for n, edges in testCases:
            print('edges: %s' % (edges))
            result = self.findMinHeightTrees(n, edges)
            print('result: %s' % (result))
            print('-='*20+'-')
    
if __name__ == '__main__':
    Solution().test()
