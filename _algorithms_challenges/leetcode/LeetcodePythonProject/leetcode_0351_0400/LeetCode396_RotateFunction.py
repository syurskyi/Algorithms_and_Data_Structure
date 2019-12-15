'''
Created on Apr 4, 2017

@author: MT
'''

class Solution(object):
    def maxRotateFunction(self, A):
        nums = A
        sumVal = 0
        sample = 0
        for i, num in enumerate(nums):
            sample += i*num
            sumVal += num
        maxVal = sample
        for i in range(len(nums)-1, 0, -1):
            sample = sample+sumVal-len(nums)*nums[i]
            maxVal = max(maxVal, sample)
        return maxVal

    def test(self):
        testCases = [
            [4, 3, 2, 6],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.maxRotateFunction(nums)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
