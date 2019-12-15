'''
Created on Dec 20, 2018

@author: tongq
'''
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m-2):
            for j in range(n-2):
                if self.isValid(grid, i, j):
                    res += 1
        return res
    
    def isValid(self, grid, i, j):
        hashset = set([grid[i][j], grid[i][j+1], grid[i][j+2],\
                       grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],\
                       grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]])
        if hashset != set(range(1, 10)):
            return False
        val = grid[i][j] + grid[i+1][j] + grid[i+2][j]
        if val != grid[i][j] + grid[i][j+1] + grid[i][j+2] or\
            val != grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] or\
            val != grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] or\
            val != grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] or\
            val != grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] or\
            val != grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] or\
            val != grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]:
            return False
        return True
    
    def test(self):
        testCases = [
            [[4,3,8,4],[9,5,1,9],[2,7,6,2]],
        ]
        for grid in testCases:
            result = self.numMagicSquaresInside(grid)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
