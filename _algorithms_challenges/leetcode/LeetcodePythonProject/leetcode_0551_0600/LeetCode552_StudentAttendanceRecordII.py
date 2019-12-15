'''
Created on Aug 23, 2017

@author: MT
'''

class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        import numpy
        matrix = numpy.matrix(
            [
                [0, 0, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [0, 1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 1],
            ]
        )
        power = matrix
        mod = 10**9+7
        while n:
            if n & 1:
                power = (power*matrix)%mod
            matrix = matrix**2 % mod
            n /= 2
        return int(power[5, 2])
    
    def checkRecord_slow(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9+7
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]
        for i in range(2):
            for j in range(3):
                dp[0][i][j] = 1
        for i in range(1, n+1):
            for j in range(2):
                for k in range(3):
                    val = dp[i-1][j][2]
                    if j > 0:
                        val = (val+dp[i-1][j-1][2]) % mod # A
                    if k > 0:
                        val = (val+dp[i-1][j][k-1]) % mod # L
                    dp[i][j][k] = val
        return dp[-1][-1][-1]
    
    def test(self):
        testCases = [
            2,
            3,
            4,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.checkRecord(n)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
