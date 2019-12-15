'''
Created on Mar 18, 2017

@author: MT
'''

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        hashmap = {}
        sumVal = 0
        maxLen = 0
        for i, num in enumerate(nums):
            sumVal += num
            if sumVal == k:
                maxLen = max(maxLen, i+1)
            if sumVal-k in hashmap:
                maxLen = max(maxLen, i-hashmap[sumVal-k])
            if sumVal not in hashmap:
                hashmap[sumVal] = i
        return maxLen
    
    def test(self):
        testCases = [
            ([1, -1, 5, -2, 3], 3),
            ([-2, -1, 2, 1], 1),
        ]
        for nums, k in testCases:
            print('nums: %s' % (nums))
            print('k: %s' % (k))
            result = self.maxSubArrayLen(nums, k)
            print('result: %s' % (result))
            print('-='*20+'-')
    
if __name__ == '__main__':
    Solution().test()
