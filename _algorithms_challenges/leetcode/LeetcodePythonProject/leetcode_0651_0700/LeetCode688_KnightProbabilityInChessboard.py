'''
Created on Oct 23, 2017

@author: MT
'''
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp = [[1]*N for _ in range(N)]
        for _ in range(K):
            dp1 = [[0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for row, col in (i+2, j-1), (i+2, j+1),\
                        (i-2, j-1), (i-2, j+1), (i+1, j-2), (i+1, j+2),\
                        (i-1, j+2), (i-1, j-2):
                        if 0 <= row < N and 0 <= col < N:
                            dp1[i][j] += dp[row][col]
            dp = dp1
        return float(dp[r][c])/8**K
    
    def test(self):
        testCases = [
            [3, 2, 0, 0],
        ]
        for N, K, r, c in testCases:
            print('n: %s' % N)
            print('K: %s' % K)
            print('r: %s' % r)
            print('c: %s' % c)
            result = self.knightProbability(N, K, r, c)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
