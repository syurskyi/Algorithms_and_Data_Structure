'''
Created on Oct 21, 2017

@author: MT
'''
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        roots = [-1]*(n+1)
        for edge in edges:
            root1 = self.getRoot(roots, edge[0])
            root2 = self.getRoot(roots, edge[1])
            if root1 == root2:
                return edge
            roots[root1] = root2
        return [-1, -1]
    
    def getRoot(self, roots, ind):
        while roots[ind] != -1:
            ind = roots[ind]
        return ind
    
    def test(self):
        testCases = [
            [[1, 2], [1, 3], [2, 3]],
            [[1, 2,], [2, 3], [3, 4], [1, 4], [1, 5]],
        ]
        for edges in testCases:
            print('edges: %s' % edges)
            result = self.findRedundantConnection(edges)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
