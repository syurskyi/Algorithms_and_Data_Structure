'''
Created on Feb 26, 2017

@author: MT
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        length = len(nums)
        result = []
        result.append(1)
        for i in range(1, length):
            result.append(result[-1]*nums[i-1])
        right = 1
        for i in range(length-2, -1, -1):
            right *= nums[i+1]
            result[i] = right*result[i]
        return result
    
    def productExceptSelfExtra(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        length = len(nums)
        left = [1]*length
        right = [1]*length
        for i in range(1, length):
            left[i] = left[i-1]*nums[i-1]
        for i in range(length-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        result = []
        print('left:  %s' % left)
        print('right: %s' % right)
        for i in range(length):
            result.append(left[i]*right[i])
        return result
    
    def test(self):
        testCases = [
            [1, 2, 3, 4],
            [9, 0, -2],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.productExceptSelf(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
