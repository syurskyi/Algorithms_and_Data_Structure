'''
Created on Apr 17, 2017

@author: MT
'''

class Solution(object):
    def findDuplicates(self, nums):
        result = []
        for num in nums:
            ind = abs(num)-1
            if nums[ind] < 0:
                result.append(abs(num))
            else:
                nums[ind] = -nums[ind]
        return result
    
    def test(self):
        testCases = [
            [4,3,2,7,8,2,3,1],
            [10,2,5,10,9,1,1,4,3,7],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.findDuplicates(nums)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
