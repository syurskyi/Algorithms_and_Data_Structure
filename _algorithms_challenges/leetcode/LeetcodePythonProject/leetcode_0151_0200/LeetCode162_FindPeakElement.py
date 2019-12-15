'''
Created on Feb 12, 2017

@author: MT
'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        start, end = 0, len(nums)-1
        while start < end:
            mid = int((start+end)/2)
            if (mid == 0 and nums[mid] > nums[mid+1]) or (mid == len(nums)-1 and nums[mid] > nums[mid-1]):
                return mid
            else:
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid] < nums[mid+1]:
                    start = mid+1
                else:
                    end = mid-1
        return start
    
    def test(self):
        testCases = [
            [1, 2, 3, 1],
            [1, 8, 2, 1, 3, 4],
            [2, 9, 3, 1, 0],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.findPeakElement(nums)
            print('result: %s' % (result))
            print('-='*20 + '-')

if __name__ == '__main__':
    Solution().test()