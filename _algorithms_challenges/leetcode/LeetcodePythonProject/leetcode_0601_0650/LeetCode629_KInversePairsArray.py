'''
Created on Sep 10, 2017

@author: MT
'''
class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        mod = 10**9+7
        if k > n*(n-1)//2 or k < 0:
            return 0
        if k == 0 or k == n*(n-1)//2:
            return 1
        dp = [[0]*(k+1) for _ in range(n+1)]
        dp[2][0] = 1
        dp[2][1] = 1
        for i in range(3, n+1):
            dp[i][0] = 1
            for j in range(1, min(k, i*(i-1)//2)+1):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
                if j >= i:
                    dp[i][j] -= dp[i-1][j-i]
                dp[i][j] = (dp[i][j]+mod)%mod
        return dp[-1][-1]
    
    def kInversePairs_another(self, n, k):
        mod = 10**9+7
        dp = [0]+[1]*(k+1)
        for i in range(2, n+1):
            new = [0]
            for j in range(k+1):
                v = dp[j+1]
                if j >= i:
                    v -= dp[j-i+1]
                new.append((new[-1]+v)%mod)
            dp = new
        return (dp[k+1]-dp[k])%mod
    
    def test(self):
        testCases = [
            (3, 0),
            (3, 1),
            (3, 2),
        ]
        for n, k in testCases:
            print('n: %s' % n)
            print('k: %s' % k)
            result = self.kInversePairs(n, k)
            print('result: %s' % result)
            result2 = self.kInversePairs_another(n, k)
            print('result2: %s' % result2)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
