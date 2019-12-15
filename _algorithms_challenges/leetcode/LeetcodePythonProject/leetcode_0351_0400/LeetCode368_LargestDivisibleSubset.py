'''
Created on Mar 28, 2017

@author: MT
'''

class Solution(object):
    def largestDivisibleSubset(self, nums):
        if not nums: return []
        nums.sort()
        n = len(nums)
        idx = [-1]*n
        dp = [1]*n
        maxLen = 0
        maxInd = 0
        for i in range(n):
            for j in range(i-1, -1, -1):
                if nums[i]%nums[j] == 0:
                    if dp[i]<dp[j]+1:
                        dp[i] = dp[j]+1
                        idx[i] = j
            if dp[i] > maxLen:
                maxLen = dp[i]
                maxInd = i
        ind = maxInd
        res = []
        while ind != -1:
            res.insert(0, nums[ind])
            ind = idx[ind]
        return res
    
    def test(self):
        testCases = [
            [1, 2, 3],
            [1, 2, 3, 8],
            [1, 2, 4, 8],
            [5, 7],
            [4, 8, 10, 240],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.largestDivisibleSubset(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
