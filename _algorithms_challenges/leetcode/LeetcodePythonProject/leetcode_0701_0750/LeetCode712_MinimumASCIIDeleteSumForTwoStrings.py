'''
Created on Oct 29, 2017

@author: MT
'''
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        n1, n2 = len(s1), len(s2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(n1):
            dp[i+1][0] = dp[i][0] + ord(s1[i])
        for j in range(n2):
            dp[0][j+1] = dp[0][j] + ord(s2[j])
        for i in range(n1):
            for j in range(n2):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j]+ord(s2[j]), dp[i][j+1]+ord(s1[i]))
        return dp[-1][-1]
    
    def test(self):
        testCases = [
            [
                'sea',
                'eat',
            ],
            [
                'delete',
                'leet',
            ],
        ]
        for s1, s2 in testCases:
            print('s1: %s' % s1)
            print('s2: %s' % s2)
            result = self.minimumDeleteSum(s1, s2)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
