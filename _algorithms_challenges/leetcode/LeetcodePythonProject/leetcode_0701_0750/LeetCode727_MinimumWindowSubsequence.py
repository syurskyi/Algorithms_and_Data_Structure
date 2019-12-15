'''
Created on Mar 4, 2018

@author: tongq
'''
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        t, s = T, S
        m, n = len(t), len(s)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for j in range(n+1):
            dp[0][j] = j+1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        start = 0
        length = n+1
        for j in range(1, n+1):
            if dp[m][j] != 0:
                if j-dp[m][j]+1 < length:
                    start = dp[m][j]-1
                    length = j-dp[m][j]+1
        print('dp:')
        print('\n'.join([str(row) for row in dp]))
        return '' if length==n+1 else s[start:start+length]
    
    def test(self):
        testCases = [
            [
                'abcdebdde',
                'bde',
            ],
        ]
        for s, t in testCases:
            print('s: %s' % s)
            print('t: %s' % t)
            result = self.minWindow(s, t)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
