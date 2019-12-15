'''
Created on Apr 12, 2017

@author: MT
'''

class Solution(object):
    def canPartition(self, nums):
        sumVal = sum(nums)
        if sumVal%2 != 0:
            return False
        target = sumVal//2
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for i in range(target, -1, -1):
                if i-num >= 0 and dp[i-num]:
                    dp[i] = True
        return dp[-1]
    
    def test(self):
        testCases = [
            [1, 2, 5],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.canPartition(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
