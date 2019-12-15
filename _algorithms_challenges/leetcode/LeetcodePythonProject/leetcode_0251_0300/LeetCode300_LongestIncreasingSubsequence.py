'''
Created on Mar 9, 2017

@author: MT
'''

class Solution(object):
    def lengthOfLIS(self, nums):
        import bisect
        dp = [0]*len(nums)
        length = 0
        for num in nums:
            i = bisect.bisect_left(dp, num, 0, length)
            dp[i] = num
            if i == length:
                length+=1
        print('dp: %s' % dp)
        return length
    
    def test(self):
        testCases = [
            [10, 9, 2, 5, 3, 7, 101, 18],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.lengthOfLIS(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
