'''
Created on Apr 24, 2018

@author: tongq
'''
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        rows = [[0, 0] for _ in range(m)]
        cols = [[0, 0] for _ in range(n)]
        sumVal = 0
        for i in range(m):
            for j in range(n):
                sumVal += grid[i][j]
                if grid[i][j] > rows[i][0]:
                    rows[i][1] = j
                    rows[i][0] = grid[i][j]
                if grid[i][j] > cols[j][0]:
                    cols[j][1] = i
                    cols[j][0] = grid[i][j]
        res = 0
        for i in range(m):
            for j in range(n):
                res += min(rows[i][0], cols[j][0])
        return res - sumVal
    
    def test(self):
        testCases = [
            [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]],
        ]
        for grid in testCases:
            result = self.maxIncreaseKeepingSkyline(grid)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
