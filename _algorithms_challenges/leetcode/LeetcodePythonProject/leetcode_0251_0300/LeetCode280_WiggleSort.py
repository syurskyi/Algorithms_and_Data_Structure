'''
Created on Mar 5, 2017

@author: MT
'''

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(1, length):
            if i%2 == 1 and nums[i-1] > nums[i]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            elif i%2 == 0 and nums[i-1] < nums[i]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
    
    def test(self):
        testCases = [
            [3, 5, 2, 1, 6, 4],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            self.wiggleSort(nums)
            print('after sort: %s' % (nums))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
