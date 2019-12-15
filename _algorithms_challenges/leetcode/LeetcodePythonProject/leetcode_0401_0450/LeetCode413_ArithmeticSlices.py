'''
Created on Apr 11, 2017

@author: MT
'''

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        nums = A
        if not nums or len(nums) < 3: return 0
        res = 0
        curr = 0
        for i in range(2, len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                curr += 1
            else:
                curr = 0
            res += curr
        return res
    
    def test(self):
        testCases = [
            [1, 2, 3, 4],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.numberOfArithmeticSlices(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
