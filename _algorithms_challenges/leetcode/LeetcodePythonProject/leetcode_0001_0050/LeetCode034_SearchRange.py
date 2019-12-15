'''
Created on Oct 31, 2017

@author: MT
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums)
        res = [float('inf'), float('-inf')]
        while l < r:
            mid = (l+r)//2
            if target == nums[mid]:
                res[1] = max(res[1], mid)
                l = mid+1
            elif target < nums[mid]:
                r = mid
            else:
                l = mid+1
        l, r = 0, len(nums)
        while l < r:
            mid = (l+r)//2
            if target == nums[mid]:
                res[0] = min(res[0], mid)
                r = mid
            elif target < nums[mid]:
                r = mid
            else:
                l = mid+1
        if r == len(nums):
            return [-1, -1]
        return res if res != [float('inf'), float('-inf')] else [-1, -1]
    
    def test(self):
        testCases = [
            [
                [1, 1],
                0,
            ],
            [
                [1, 1],
                1,
            ],
            [
                [1, 1],
                2,
            ],
            [
                [5, 7, 7, 8, 8, 10],
                8,
            ]
        ]
        for nums, target in testCases:
            print('nums: %s' % nums)
            print('target: %s' % target)
            result = self.searchRange(nums, target)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
