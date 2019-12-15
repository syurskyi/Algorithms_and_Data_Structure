'''
Created on Oct 16, 2019

@author: tongq
'''
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        res = 0
        for i in range(n):
            maxNum = 0
            for j in range(n):
                if grid[i][j]:
                    res += 1
                maxNum = max(maxNum, grid[i][j])
            res += maxNum
        for j in range(n):
            maxNum = 0
            for i in range(n):
                maxNum = max(maxNum, grid[i][j])
            res += maxNum
        return res
    
    def test(self):
        testCases = [
            [[2]],
            [[1,0],[0,2]],
            [[1,1,1],[1,0,1],[1,1,1]],
        ]
        for grid in testCases:
            res = self.projectionArea(grid)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
