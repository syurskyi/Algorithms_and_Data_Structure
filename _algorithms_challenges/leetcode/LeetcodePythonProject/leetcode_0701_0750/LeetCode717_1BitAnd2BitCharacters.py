'''
Created on Oct 30, 2017

@author: MT
'''
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if not bits: return False
        n = len(bits)
        if n == 1: return True
        dp = [1]*n
        i = 0
        while i < n:
            if bits[i] == 1:
                i += 2
            else:
                if i > 0:
                    dp[i] += dp[i-1]
                i += 1
        return dp[-1] > 1
    
    def test(self):
        testCases = [
            [1, 0, 0],
            [1, 1, 1, 0],
        ]
        for bits in testCases:
            print('bits: %s' % bits)
            result = self.isOneBitCharacter(bits)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
