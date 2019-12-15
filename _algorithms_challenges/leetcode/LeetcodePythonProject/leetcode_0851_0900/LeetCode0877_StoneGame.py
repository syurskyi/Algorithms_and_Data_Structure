'''
Created on Oct 8, 2019

@author: tongq
'''
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for d in range(1, n):
            for i in range(n-d):
                dp[i][i+d] = max(piles[i]-dp[i+1][i+d], piles[i+d]-dp[i][i+d-1])
        return dp[0][-1] > 0
    
    def test(self):
        testCases = [
            [3,7,2,3],
            [5,3,4,5],
        ]
        for piles in testCases:
            res = self.stoneGame(piles)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
