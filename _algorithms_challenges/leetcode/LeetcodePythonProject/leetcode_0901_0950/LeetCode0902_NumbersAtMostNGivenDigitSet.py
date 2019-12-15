class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        s = str(N)
        k = len(s)
        dp = [0]*k + [1]
        for i in range(k-1, -1, -1):
            for d in D:
                if d < s[i]:
                    dp[i] += len(D)**(k-i-1)
                elif d == s[i]:
                    dp[i] += dp[i+1]
        return dp[0] + sum(len(D)**i for i in range(1, k))

    def test(self):
        testCases = [
            # [["3","4","8"], 4],
            # [['7'], 8],
            # [["1","3","5","7"], 100],
            [["1","4","9"], 1000000000],
        ]
        for d, n in testCases:
            res = self.atMostNGivenDigitSet(d, n)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
