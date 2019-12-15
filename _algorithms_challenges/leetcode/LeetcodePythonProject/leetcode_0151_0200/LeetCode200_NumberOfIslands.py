'''
Created on Feb 16, 2017

@author: MT
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '#'
                    res += 1
                    self.bfs(grid, i, j)
        return res
    
    def bfs(self, grid, i, j):
        queue = [(i, j)]
        m, n = len(grid), len(grid[0])
        while queue:
            i, j = queue.pop(0)
            for x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    grid[x][y] = '#'
                    queue.append([x, y])
    
    def test(self):
        testCases = [
#             [
#                 '11110',
#                 '11010',
#                 '11000',
#                 '00000',
#             ],
            [
                '11000',
                '11000',
                '00100',
                '00011',
            ],
        ]
        for grid in testCases:
            grid = [list(x) for x in grid]
            result = self.numIslands(grid)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
