'''
Created on Aug 28, 2017

@author: MT
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = len(nums)-1
        while j > 0 and nums[j-1] >= nums[j]:
            j -= 1
        self.reverse(nums, j, len(nums)-1)
        if j == 0:
            return
        i = j-1
        while j+1 < len(nums) and nums[i] >= nums[j]:
            j += 1
        nums[i], nums[j] = nums[j], nums[i]
    
    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    
    def test(self):
        testCases = [
            [1, 2, 3],
            [3, 2, 1],
            [1, 1, 5],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            self.nextPermutation(nums)
            print('nums: %s' % nums)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
