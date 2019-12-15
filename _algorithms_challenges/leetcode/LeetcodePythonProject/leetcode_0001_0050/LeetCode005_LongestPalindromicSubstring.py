'''
Created on Jan 7, 2017

@author: MT
'''

class Solution(object):
    def longestPalindromeDP(self, s):
        res = ''
        if not s: return res
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i-j<=1 or dp[i-1][j+1]):
                    dp[i][j] = True
                    if i-j+1 > len(res):
                        res = s[j:i+1]
        return res
    
    def longestPalindromeDP_another(self, s):
        if not s: return s
        length = len(s)
        maxLen = 1
        table = [[False,]*length for _ in range(length)]
        longest = s[0]
        for l in range(length):
            for i in range(length-l):
                j = i+l
                if s[i] == s[j] and (j-i<=2 or table[i+1][j-1]):
                    table[i][j] = True
                    if j-i+1 > maxLen:
                        maxLen = j-i+1
                        longest = s[i:j+1]
        return longest
    
    def test(self):
        testCases = [
            'babad',
            'cbbd',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.longestPalindromeDP(s)
            print('result: %s' % (result))
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()
