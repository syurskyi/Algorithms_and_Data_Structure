'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object):
    def islandPerimeter(self, grid):
        result = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += self.getParameter(i, j, grid)
        return result
    
    def getParameter(self, i, j, grid):
        m, n = len(grid), len(grid[0])
        p = 4
        for x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1):
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                p -= 1
        return p
