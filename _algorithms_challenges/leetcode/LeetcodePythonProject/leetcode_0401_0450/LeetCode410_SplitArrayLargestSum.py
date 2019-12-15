'''
Created on Apr 10, 2017

@author: MT
'''

class Solution(object):
    def splitArray(self, nums, m):
        left, right = 0, 0
        for num in nums:
            left = max(left, num)
            right += num
        while left < right:
            mid = (left+right)//2
            if self.doable(nums, m-1, mid):
                right = mid
            else:
                left = mid+1
        return left
    
    def doable(self, nums, cuts, maxVal):
        acc = 0
        for num in nums:
            if num > maxVal:
                return False
            elif acc+num <= maxVal:
                acc += num
            else:
                cuts -= 1
                acc = num
                if cuts < 0:
                    return False
        return True
    
    def test(self):
        testCases = [
            [
                [7,2,5,10,8],
                2,
            ],
        ]
        for nums, m in testCases:
            print('nums: %s' % nums)
            print('m: %s' % m)
            result = self.splitArray(nums, m)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
