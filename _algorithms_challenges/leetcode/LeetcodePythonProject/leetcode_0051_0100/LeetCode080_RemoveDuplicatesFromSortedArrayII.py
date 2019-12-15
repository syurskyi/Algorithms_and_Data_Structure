'''
Created on Jan 24, 2017

@author: MT
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        prev, curr = 1, 2
        while curr < len(nums):
            if nums[curr] != nums[prev] or nums[curr] != nums[prev-1]:
                prev += 1
                nums[prev] = nums[curr]
            curr += 1
        return prev + 1
    
    def test(self):
        pass

if __name__ == '__main__':
    Solution().test()
