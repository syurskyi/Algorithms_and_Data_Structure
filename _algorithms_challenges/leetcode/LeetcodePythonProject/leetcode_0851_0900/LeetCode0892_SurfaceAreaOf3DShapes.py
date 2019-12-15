'''
Created on Oct 31, 2019

@author: tongq
'''
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if (grid[i][j]):
                    res += 2+grid[i][j]*4
                if i > 0:
                    res -= min(grid[i-1][j], grid[i][j])*2
                if j > 0:
                    res -= min(grid[i][j-1], grid[i][j])*2
        return res
    
    def test(self):
        testCases = [
            [[1,0],[0,2]],
            [[1,1,1],[1,0,1],[1,1,1]],
            [[2,2,2],[2,1,2],[2,2,2]],
        ]
        for grid in testCases:
            res = self.surfaceArea(grid)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
