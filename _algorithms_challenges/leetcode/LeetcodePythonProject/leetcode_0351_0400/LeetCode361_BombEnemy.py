'''
Created on Mar 27, 2017

@author: MT
'''

class Solution(object):
    def maxKilledEnemies(self, grid):
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        res = 0
        rows = 0
        cols = [0]*n
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == 'W':
                    rows = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W': break
                        if grid[i][k] == 'E': rows += 1
                if i == 0 or grid[i-1][j] == 'W':
                    cols[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W': break
                        if grid[k][j] == 'E': cols[j] += 1
                if grid[i][j] == '0':
                    res = max(res, cols[j]+rows)
        return res
