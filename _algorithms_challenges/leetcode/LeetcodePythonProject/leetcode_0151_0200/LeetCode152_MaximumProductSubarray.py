'''
Created on Feb 11, 2017

@author: MT
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxArr, minArr = [0]*n, [0]*n
        maxArr[0], minArr[0] = nums[0], nums[0]
        result = nums[0]
        for i in range(1, n):
            num = nums[i]
            if num > 0:
                maxArr[i] = max(maxArr[i-1]*num, num)
                minArr[i] = min(minArr[i-1]*num, num)
            else:
                maxArr[i] = max(minArr[i-1]*num, num)
                minArr[i] = min(maxArr[i-1]*num, num)
            result = max(result, maxArr[i])
        return result
    
    def test(self):
        testCases = [
            [2, 3, -2, 4],
            [1, 0, 9, 10, -19, 2000],
            [100, 2, -1, 9, 89, -1, -1, 9],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.maxProduct(nums)
            print('result: %s' % (result))
            print('-='*20 + '-')

if __name__ == '__main__':
    Solution().test()
