'''
Created on Sep 4, 2017

@author: MT
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[float('inf')]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = dp[i][j-1]+1
                elif j == 0:
                    dp[i][j] = dp[i-1][j]+1
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[-1][-1]
    
    def test(self):
        testCases = [
            [
                'sea',
                'eat',
            ],
            [
                '',
                'abc',
            ],
        ]
        for word1, word2 in testCases:
            print('word1: %s' % word1)
            print('word2: %s' % word2)
            result = self.minDistance(word1, word2)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
