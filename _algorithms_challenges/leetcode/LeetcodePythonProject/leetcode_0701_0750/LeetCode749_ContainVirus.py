'''
Created on Mar 24, 2018

@author: tongq
'''
class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cost = [0]
        while self.check(grid, cost):
            continue
        return cost[0]
    
    def check(self, grid, cost):
        count = 1
        maxVal = -1
        flag = False
        info = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                    walls = [[0]*n for _ in range(m)]
                    res = [0, 0]
                    grid[i][j] = count
                    self.dfs(i, j, grid, count, walls, res)
                    if res[0] != 0:
                        flag = True
                    if maxVal == -1 or res[0] > info[maxVal][0]:
                        maxVal = count-2
                    info.append(list(res))
        if count == 1:
            return False
        cost[0] += info[maxVal][1]
        self.update(grid, maxVal+2)
        return flag
    
    def dfs(self, row, col, grid, count, walls, res):
        shiftX = [1, 0, -1, 0]
        shiftY = [0, 1, 0, -1]
        m, n = len(grid), len(grid[0])
        for i in range(4):
            newRow = row+shiftX[i]
            newCol = col+shiftY[i]
            if 0 <= newRow < m and 0 <= newCol < n:
                if grid[newRow][newCol] == 1:
                    grid[newRow][newCol] = count
                    self.dfs(newRow, newCol, grid, count, walls, res)
                elif grid[newRow][newCol] == 0:
                    if walls[newRow][newCol] == 0:
                        res[0] += 1
                    if (walls[newRow][newCol] & 1 << i) == 0:
                        res[1] += 1
                        walls[newRow][newCol] |= 1 << i
    
    def update(self, grid, quarantine):
        shiftX = [1, 0, -1, 0]
        shiftY = [0, 1, 0, -1]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 1 and grid[i][j] != quarantine:
                    for k in range(4):
                        newRow = i+shiftX[k]
                        newCol = j+shiftY[k]
                        if 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] == 0:
                            grid[newRow][newCol] = 1
                    grid[i][j] = 1
                elif grid[i][j] == quarantine:
                    grid[i][j] = -1
    
    def test(self):
        testCases = [
            [
                [0,1,0,0,0,0,0,1],
                [0,1,0,1,0,0,0,1],
                [0,0,0,0,0,0,0,1],
            ],
            [
                [0,1,0,0,0,0,0,1],
                [0,1,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,0]
            ],
            [
                [1,1,1],
                [1,0,1],
                [1,1,1]
            ],
            [
                [1,1,1,0,0,0,0,0,0],
                [1,0,1,0,1,1,1,1,1],
                [1,1,1,0,0,0,0,0,0]
            ],
        ]
        for grid in testCases:
            result = self.containVirus(grid)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
