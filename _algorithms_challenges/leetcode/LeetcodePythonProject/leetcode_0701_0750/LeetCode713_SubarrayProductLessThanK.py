'''
Created on Oct 29, 2017

@author: MT
'''
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1: return 0
        prod = 1
        left = 0
        count = 0
        for i, num in enumerate(nums):
            prod *= num
            while left < i+1 and prod >= k:
                prod //= nums[left]
                left += 1
            count += i-left+1
        return count
    
    def test(self):
        testCases = [
            [
                [10, 5, 2, 6],
                100,
            ],
        ]
        for nums, k in testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = self.numSubarrayProductLessThanK(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
