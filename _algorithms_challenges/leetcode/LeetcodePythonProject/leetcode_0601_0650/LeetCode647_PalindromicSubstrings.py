'''
Created on Oct 1, 2017

@author: MT
'''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i-j<=1 or dp[i-1][j+1]):
                    dp[i][j] = True
                    res += 1
        return res
    
    def test(self):
        testCases = [
            'abc',
            'aaa',
            'aaaaa',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.countSubstrings(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
