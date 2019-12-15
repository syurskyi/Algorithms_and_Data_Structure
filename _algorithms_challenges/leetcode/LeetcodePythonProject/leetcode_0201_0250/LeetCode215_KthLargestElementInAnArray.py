'''
Created on Feb 20, 2017

@author: MT
'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import random
        random.shuffle(nums)
        if k < 1 or not nums:
            return 0
        k = len(nums)-k
        return self.helper(nums, 0, len(nums)-1, k)
    
    def helper(self, nums, i, j, k):
        i0, j0 = i, j
        pivot = nums[j]
        while True:
            while i < j and nums[i] < pivot:
                i += 1
            while i < j and nums[j] >= pivot:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break
        nums[i], nums[j0] = nums[j0], nums[i]
        if i == k:
            return nums[i]
        elif i < k:
            return self.helper(nums, i+1, j0, k)
        else:
            return self.helper(nums, i0, i-1, k)
    
    def findKthLargestHeap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heapq.heapify(nums)
        for _ in range(len(nums)-k+1):
            result = heapq.heappop(nums)
        return result
    
    def test(self):
        testCases = [
            ([2, 1], 1),
            ([3,2,1,5,6,4], 5),
            ([3,3,3,3,3,3], 1),
        ]
        for nums, k in testCases:
            print('nums: %s' % (nums))
            print('k: %s' % (k))
            result = self.findKthLargest(nums, k)
            print('result: %s' % (result))
            resultHeap = self.findKthLargestHeap(nums, k)
            print('resultHeap: %s' % (resultHeap))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
