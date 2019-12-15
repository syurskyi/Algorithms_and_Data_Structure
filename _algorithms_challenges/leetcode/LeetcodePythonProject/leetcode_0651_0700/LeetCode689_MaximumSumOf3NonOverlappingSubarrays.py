'''
Created on Oct 23, 2017

@author: MT
'''
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        dp = [[0]*(n+1) for _ in range(4)]
        sumVal = 0
        accu = [0]*(n+1)
        for i in range(n):
            sumVal += nums[i]
            accu[i] = sumVal
        ids = [[0]*(n+1) for _ in range(4)]
        for i in range(1, 4):
            for j in range(k-1, n):
                tmpMax = accu[j] if j-k<0 else accu[j]-accu[j-k]+dp[i-1][j-k]
                if j >= k:
                    dp[i][j] = dp[i][j-1]
                    ids[i][j] = ids[i][j-1]
                if j > 0 and tmpMax > dp[i][j-1]:
                    dp[i][j] = tmpMax
                    ids[i][j] = j-k+1
        res = [0]*3
        res[2] = ids[3][n-1]
        res[1] = ids[2][res[2]-1]
        res[0] = ids[1][res[1]-1]
        return res
    
    def test(self):
        testCases = [
            [
                [1,2,1,2,6,7,5,1],
                2,
            ],
            [
                [7,13,20,19,19,2,10,1,1,19],
                3,
            ],
        ]
        for nums, k in testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = self.maxSumOfThreeSubarrays(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
