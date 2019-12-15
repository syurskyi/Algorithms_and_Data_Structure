'''
Created on Feb 8, 2017

@author: MT
'''

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        cuts = list(range(n))
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i-j<=1 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if j > 0:
                        cuts[i] = min(cuts[i], cuts[j-1]+1)
                    else:
                        cuts[i] = 0
        return cuts[-1]
    
    def test(self):
        testCases = [
            'abba',
            'aab',
            'aca'
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.minCut(s)
            print('result: %s' % (result))
            print('-='*20+'-')
    
if __name__ == '__main__':
    Solution().test()
