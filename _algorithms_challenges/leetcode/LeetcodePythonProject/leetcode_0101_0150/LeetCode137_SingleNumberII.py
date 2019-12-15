'''
Created on Feb 9, 2017

@author: MT
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num1, num2 = 0, 0
        for num in nums:
            num2 ^= num1 & num
            num1 ^= num
            mask = ~(num1 & num2)
            num2 &= mask
            num1 &= mask
        return num1
    
    def test(self):
        testCases = [
            [1, 2, 1, 1, 3, 3, 3],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.singleNumber(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()