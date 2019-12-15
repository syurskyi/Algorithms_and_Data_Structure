'''
Created on Apr 11, 2017

@author: MT
'''

class Solution(object):
    def thirdMax(self, nums):
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif first > num > second:
                third = second
                second = num
            elif second > num > third:
                third = num
        return third if third != float('-inf') else first
    
    def test(self):
        testCases = [
            [2, 2, 3, 1],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.thirdMax(nums)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
