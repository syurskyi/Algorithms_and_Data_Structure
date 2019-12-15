'''
Created on Mar 8, 2017

@author: MT
'''

class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo = {}
        return self.helper(s, memo)
    
    def helper(self, s, memo):
        if s in memo:
            return memo[s]
        otherWin = True
        for i in range(len(s)-1):
            if s[i:i+2] == '++':
                s0 = s[:i]+'--'+s[i+2:]
                if not self.helper(s0, memo):
                    otherWin = False
                    break
        memo[s] = not otherWin
        return memo[s]
    
    def test(self):
        testCases = [
            '++++',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.canWin(s)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
