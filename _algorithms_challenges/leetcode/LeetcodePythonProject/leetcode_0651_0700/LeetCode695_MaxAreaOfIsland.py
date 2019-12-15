'''
Created on Oct 25, 2017

@author: MT
'''
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        maxArea = 0
        for i in range(m):
            for j in range(n):
                maxArea = max(maxArea, self.bfs(grid, m, n, i, j))
        return maxArea
    
    def bfs(self, grid, m, n, i, j):
        if grid[i][j] == 0:
            return 0
        area = 0
        grid[i][j] = -1
        queue = [(i, j)]
        while queue:
            i, j = queue.pop(0)
            area += 1
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    queue.append((x, y))
                    grid[x][y] = -1
        return area
    
    def test(self):
        testCases = [
            [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]],
        ]
        for grid in testCases:
            result = self.maxAreaOfIsland(grid)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
