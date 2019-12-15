'''
Created on Apr 1, 2017

@author: MT
'''

class Solution(object):
    def wiggleMaxLength(self, nums):
        if not nums: return 0
        maxLen = 1
        i = 1
        while i < len(nums):
            if nums[i] > nums[i-1]:
                while i+1 < len(nums) and nums[i] <= nums[i+1]:
                    i += 1
                maxLen += 1
            elif nums[i-1] > nums[i]:
                while i+1 < len(nums) and nums[i+1] <= nums[i]:
                    i += 1
                maxLen += 1
            i += 1
        return maxLen
    
    def test(self):
        testCases = [
            [1,7,4,9,2,5],
            [1,17,5,10,13,15,10,5,16,8],
            [1,2,3,4,5,6,7,8,9],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.wiggleMaxLength(nums)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
