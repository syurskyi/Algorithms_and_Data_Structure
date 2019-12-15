'''
Created on Mar 16, 2017

@author: MT
'''

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        distance = [[0]*n for _ in range(m)]
        reach = [[0]*n for _ in range(m)]
        buildingNum = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildingNum += 1
                    queue = [(i, j)]
                    visited = [[False]*n for _ in range(m)]
                    level = 1
                    while queue:
                        size = len(queue)
                        for _ in range(size):
                            i0, j0 = queue.pop(0)
                            for x, y in (i0+1, j0), (i0-1, j0), (i0, j0+1), (i0, j0-1):
                                if 0 <= x < m and 0 <= y < n and\
                                    not visited[x][y] and grid[x][y] == 0:
                                    distance[x][y] += level
                                    reach[x][y] += 1
                                    visited[x][y] = True
                                    queue.append((x, y))
                        level += 1
        res = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[i][j] == buildingNum:
                    res = min(res, distance[i][j])
        return res if res != float('inf') else -1
    
    def test(self):
        testCases = [
            [
                [1, 0, 2, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
            ]
        ]
        for grid in testCases:
            result = self.shortestDistance(grid)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
