'''
Created on Mar 19, 2017

@author: MT
'''

class Solution(object):
    def increasingTriplet(self, nums):
        if not nums: return False
#         first = float('inf')
        first = nums[0]
        second = float('inf')
        for i in range(1, len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True
        return False
    
    def test(self):
        testCases = [
            [1, 2, 3],
            [5, 4, 3, 2, 1],
            [1, 9, 10, 3],
            [10, 9, 8, 7, 100, 1, 2, 5],
            [1, 0, 10, 0, 1000],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,3],
            [1, 2, 1, 0],
            [2, 1, 3],
            [3, 2, 1, 9],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.increasingTriplet(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

