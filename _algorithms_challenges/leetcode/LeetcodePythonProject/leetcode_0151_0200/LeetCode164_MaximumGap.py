'''
Created on Feb 12, 2017

@author: MT
'''
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        if not nums or len(nums) < 2:
            return 0
        minVal = min(nums)
        maxVal = max(nums)
        n = len(nums)
        gap = math.ceil(float(maxVal-minVal)/(n-1))
        bucketsMin = [float('inf')]*(n-1)
        bucketsMax = [float('-inf')]*(n-1)
        for num in nums:
            if num == minVal or num == maxVal:
                continue
            idx = int((num-minVal)//gap)
            bucketsMin[idx] = min(bucketsMin[idx], num)
            bucketsMax[idx] = max(bucketsMax[idx], num)
        maxGap = float('-inf')
        prev = minVal
        for i in range(n-1):
            if bucketsMin[i] == float('inf') and bucketsMax[i] == float('-inf'):
                continue
            maxGap = max(maxGap, bucketsMin[i]-prev)
            prev = bucketsMax[i]
        maxGap = max(maxGap, maxVal-prev)
        return maxGap
    
    def test(self):
        testCases = [
            [1, 1000],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.maximumGap(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()