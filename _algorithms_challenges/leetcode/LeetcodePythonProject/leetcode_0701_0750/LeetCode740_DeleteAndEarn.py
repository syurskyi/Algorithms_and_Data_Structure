'''
Created on Mar 14, 2018

@author: tongq
'''
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0]*10001
        for num in nums:
            count[num] += num
        dp = [0]*10003
        for i in range(10000, -1, -1):
            dp[i] = max(count[i]+dp[i+2], dp[i+1])
        return dp[0]
    
    def test(self):
        testCases = [
            [3, 4, 2],
            [2, 2, 3, 3, 3, 4],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.deleteAndEarn(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
