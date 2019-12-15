'''
Created on Apr 21, 2018

@author: tongq
'''
class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if not (0<=i<m and 0<=j<n) or grid[i][j]!=1:
                return 0
            res = 1
            grid[i][j] = 2
            res += sum(dfs(x, y) for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)])
            return res
        
        # Check whether (i, j) is connected to Not Failling Bricks
        def is_connected(i, j):
            return i==0 or any([0<=x<m and 0<=y<n and grid[x][y]==2\
                                for x, y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]])
        
        # Mark whether there is a brick at the each hit
        for i, j in hits:
            grid[i][j] -= 1
        
        # Get grid after all hits
        for i in range(n):
            dfs(0, i)
        
        # Reversely and the block of each hits and get count of newly add bricks
        res = [0]*len(hits)
        for k in reversed(range(len(hits))):
            i, j = hits[k]
            grid[i][j] += 1
            if grid[i][j] == 1 and is_connected(i, j):
                res[k] = dfs(i, j)-1
        return res
    
    def test(self):
        testCases = [
            [
                [
                    [1,0,0,0],
                    [1,1,1,0]
                ],
                [[1,0]],
            ],
            [
                [
                    [1,0,0,0],
                    [1,1,0,0]
                ],
                [[1,1],[1,0]],
            ],
        ]
        for grid, hits in testCases:
            print('grid: %s' % grid)
            print('hits: %s' % hits)
            result = self.hitBricks(grid, hits)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
