'''
Created on Mar 18, 2017

@author: MT
'''

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        len1, len2 = len(nums1), len(nums2)
        result = []
        for i in range(0, k+1):
            j = k-i
            if i > len1 or j > len2:
                continue
            left = self.getMax(nums1, i)
            right = self.getMax(nums2, j)
            tmpResult = self.merge(left, right)
            result = max(result, tmpResult)
        return result
    
    def getMax(self, nums, maxLen):
        result = []
        size = len(nums)
        for x in range(size):
            while result and len(result)+size-x>maxLen and result[-1]<nums[x]:
                result.pop()
            if len(result) < maxLen:
                result.append(nums[x])
        return result
    
    def merge(self, nums1, nums2):
        result = []
        while nums1 and nums2:
            if nums1 >= nums2:
                result.append(nums1.pop(0))
            else:
                result.append(nums2.pop(0))
        while nums1:
            result.append(nums1.pop(0))
        while nums2:
            result.append(nums2.pop(0))
        return result
    
    def test(self):
        testCases = [
            (
                [3, 4, 6, 5],
                [9, 1, 2, 5, 8, 3],
                5,
            ),
            (
                [9, 1, 2, 5, 8, 3],
                [3, 4, 6, 5],
                5,
            ),
            (
                [6, 7],
                [6, 0, 4],
                5,
            ),
            (
                [3, 9],
                [8, 9],
                3,
            ),
        ]
        for nums1, nums2, k in testCases:
            print('nums1: %s' % (nums1))
            print('nums2: %s' % (nums2))
            print('k: %s' % (k))
            result = self.maxNumber(nums1, nums2, k)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

