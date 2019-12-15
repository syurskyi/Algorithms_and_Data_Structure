'''
Created on Mar 20, 2018

@author: tongq
'''
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        M = (N<<1)-1
        dp = [[0]*N for _ in range(N)]
        dp[0][0] = grid[0][0]
        for n in range(1, M):
            for i in range(N-1, -1, -1):
                for p in range(N-1, -1, -1):
                    j = n-i
                    q = n-p
                    if j<0 or j>=N or q<0 or q>=N or grid[i][j]<0 or grid[p][q]<0:
                        dp[i][p] = -1
                        continue
                    if i > 0:
                        dp[i][p] = max(dp[i][p], dp[i-1][p])
                    if p > 0:
                        dp[i][p] = max(dp[i][p], dp[i][p-1])
                    if i > 0 and p > 0:
                        dp[i][p] = max(dp[i][p], dp[i-1][p-1])
                    if dp[i][p] >= 0:
                        dp[i][p] += grid[i][j]+(grid[p][q] if i!=p else 0)
        return max(dp[-1][-1], 0)
    
    def test(self):
        testCases = [
            [
                [0, 1, -1],
                [1, 0, -1],
                [1, 1,  1]
            ],
        ]
        for grid in testCases:
            result = self.cherryPickup(grid)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
