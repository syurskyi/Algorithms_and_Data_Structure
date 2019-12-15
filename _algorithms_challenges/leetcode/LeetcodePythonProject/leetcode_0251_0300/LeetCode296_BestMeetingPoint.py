'''
Created on Mar 8, 2017

@author: MT
'''

class Solution(object):
    def minTotalDistance(self, grid):
        m, n = len(grid), len(grid[0])
        rows, cols = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        cols.sort()
        sumVal = 0
        for row in rows:
            sumVal += abs(row - rows[len(rows)//2])
        for col in cols:
            sumVal += abs(col - cols[len(cols)//2])
        return sumVal
    
    def test(self):
        testCases = [
            [
                '10001',
                '00000',
                '00100',
            ],
        ]
        for grid in testCases:
            grid = [[int(x) for x in l] for l in grid]
            print('grid: %s' % (grid))
            result = self.minTotalDistance(grid)
            print('result: %s' % (result))
            print('-='*20 + '-')

if __name__ == '__main__':
    Solution().test()
