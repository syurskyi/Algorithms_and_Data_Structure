'''
Created on Feb 19, 2017

@author: MT
'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        start, end = 0, 0
        minLen = len(nums) + 1
        sumVal = 0
        while start <= end and end < len(nums):
            sumVal += nums[end]
            if sumVal >= s:
                while start <= end and sumVal >= s:
                    sumVal -= nums[start]
                    minLen = min(minLen, end-start+1)
                    start+=1
            end+=1
        if minLen > len(nums):
            return 0
        else:
            return minLen
    
    def minSubArrayLenBS(self, s, nums):
        sums = [0]*(len(nums)+1)
        for i in range(1, len(sums)):
            sums[i] = sums[i-1] + nums[i-1]
        minLen = len(nums)+1
        for i in range(len(sums)):
            end = self.binarySearch(i+1, len(sums)-1, sums[i]+s, sums)
            if end == len(sums):
                break
            minLen = min(minLen, end-i)
        return minLen if minLen <= len(nums) else 0
    
    def binarySearch(self, low, high, key, sums):
        while low <= high:
            mid = int((low+high)/2)
            if sums[mid] >= key:
                high = mid-1
            else:
                low = mid+1
        return low
    
    def test(self):
        testCases = [
            (7, [2, 3, 1, 2, 4, 3]),
            (4, [1, 4, 4]),
            (11, [1, 2, 3, 4, 5]),
        ]
        for s, nums in testCases:
            print('nums: %s' % (nums))
            print('s: %s' % (s))
            result = self.minSubArrayLen(s, nums)
            print('result: %s' % (result))
            resultBS = self.minSubArrayLenBS(s, nums)
            print('resultBS: %s' % (resultBS))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()