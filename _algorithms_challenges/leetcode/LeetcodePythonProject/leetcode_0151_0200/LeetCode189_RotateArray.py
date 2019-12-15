'''
Created on Feb 16, 2017

@author: MT
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        if k == 0: return
        arr = []
        for i0 in range(length):
            i = length + i0 - k if i0<k else i0-k
            arr.append(nums[i])
        for i in range(length):
            nums[i] = arr[i]
    
    def test(self):
        testCases = [
            ([1,2,3,4,5,6,7], 3),
        ]
        for nums, k in testCases:
            print('nums: %s' % (nums))
            print('k: %s' % (k))
            self.rotate(nums, k)
            print('after: %s' % (nums))
            print('-='*20+'-')
        
if __name__ == '__main__':
    Solution().test()