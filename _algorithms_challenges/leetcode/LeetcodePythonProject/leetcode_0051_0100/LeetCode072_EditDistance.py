'''
Created on Jan 23, 2017

@author: MT
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        dp = [[0]*(m+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        for i in range(0, n):
            c1 = word1[i]
            for j in range(0, m):
                c2 = word2[j]
                if c1 == c2:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    replace = dp[i][j] + 1
                    insert = dp[i][j+1] + 1
                    delete = dp[i+1][j] + 1
                    dp[i+1][j+1] = min((replace, insert, delete))
        return dp[-1][-1]
    
    def test(self):
        testCases = [
            ('', 'a'),
            ('horse', 'rose'),
            ('horse', 'ros'),
        ]
        for word1, word2 in testCases:
            print('word1: %s' % (word1))
            print('word2: %s' % (word2))
            result = self.minDistance(word1, word2)
            print('result: %s' % (result))
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()