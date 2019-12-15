'''
Created on Oct 21, 2017

@author: MT
'''
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        can1 = [-1, -1]
        can2 = [-1, -1]
        n = len(edges)
        parent = [0]*(n+1)
        for i in range(n):
            if parent[edges[i][1]] == 0:
                parent[edges[i][1]] = edges[i][0]
            else:
                can2 = [edges[i][0], edges[i][1]]
                can1 = [parent[edges[i][1]], edges[i][1]]
                edges[i][1] = 0
        for i in range(n+1):
            parent[i] = i
        for i in range(n):
            if edges[i][1] == 0:
                continue
            child = edges[i][1]
            par = edges[i][0]
            if self.getRoot(parent, par) == child:
                if can1[0] == -1:
                    return edges[i]
                return can1
            parent[child] = par
        return can2
    
    def getRoot(self, parent, i):
        while i != parent[i]:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    
    def test(self):
        testCases = [
#             [[1, 2], [1, 3], [2, 3]],
#             [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]],
            [[2,1],[3,1],[4,2],[1,4]],
        ]
        for edges in testCases:
            print('edges: %s' % edges)
            result = self.findRedundantDirectedConnection(edges)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
