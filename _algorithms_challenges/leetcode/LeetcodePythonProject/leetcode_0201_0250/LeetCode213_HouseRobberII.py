'''
Created on Feb 19, 2017

@author: MT
'''

class Solution(object):
    def rob(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        return max(self.robHelper(nums, 0, len(nums)-2),\
                   self.robHelper(nums, 1, len(nums)-1))
    
    def robHelper(self, nums, lo, hi):
        include, exclude = 0, 0
        for i0 in range(lo, hi+1):
            i, e = include, exclude
            include = e+nums[i0]
            exclude = max(i, e)
        return max(include, exclude)
    
    def robSpace(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) < 2: return nums[0]
        dp0 = [0]*len(nums)
        dp1 = [0]*len(nums)
        for i in range(len(nums)-1):
            if i == 0:
                dp0[i] = nums[0]
            elif i == 1:
                dp0[i] = max(nums[i], nums[i-1])
            else:
                dp0[i] = max(dp0[i-1], dp0[i-2] + nums[i])
        for i in range(1, len(nums)):
            if i == 1:
                dp1[i] = nums[i]
            elif i == 2:
                dp1[i] = max(nums[i], nums[i-1])
            else:
                dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
        return max(dp0[-2], dp1[-1])
    
    def test(self):
        testCases = [
            [1, 1, 1],
#             [1, 1],
            [1, 2, 3, 9],
            [2, 1, 1, 2]
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.rob(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
