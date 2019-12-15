'''
Created on Apr 29, 2018

@author: tongq
'''
class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        arr, k = A, K
        n = len(arr)
        memo = [[0.0]*(n+1) for _ in range(n+1)]
        cur = 0.0
        for i in range(n):
            cur += arr[i]
            memo[i+1][1] = cur/(i+1)
        return self.search(n, k, arr, memo)
    
    def search(self, n, k, arr, memo):
        if memo[n][k] > 0:
            return memo[n][k]
        if n < k:
            return 0
        cur = 0.0
        for i in range(n-1, -1, -1):
            cur += arr[i]
            memo[n][k] = max(memo[n][k], self.search(i, k-1, arr, memo)+cur/(n-i))
        return memo[n][k]
    
    def test(self):
        testCases = [
            [
                [9,1,2,3,9],
                3
            ],
        ]
        for arr, k in testCases:
            print('arr: %s' % arr)
            print('k: %s' % k)
            result = self.largestSumOfAverages(arr, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
