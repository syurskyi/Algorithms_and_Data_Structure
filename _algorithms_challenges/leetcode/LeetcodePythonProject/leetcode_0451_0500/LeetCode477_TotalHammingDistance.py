'''
Created on Apr 27, 2017

@author: MT
'''

class Solution(object):
    def totalHammingDistance(self, nums):
        res = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                if num & (1 << i):
                    cnt += 1
            res += cnt*(len(nums)-cnt)
        return res
    
    def test(self):
        testCases = [
            [4, 14, 2],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.totalHammingDistance(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
