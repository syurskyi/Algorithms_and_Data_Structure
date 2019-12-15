'''
Created on Feb 14, 2017

@author: MT
'''
#TODO: cannot do this using Python 3 because cmp is not available
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        comp = lambda a, b: 1 if a+b > b+a else -1 if a+b<b+a else 0
        nums = list(map(str, nums))
        nums.sort(cmp=comp, reverse=True)
        return ''.join(nums).lstrip('0')
    
    # @param {integer[]} nums
    # @return {string}
    def largestNumber_python2(self, nums):
        #python 2 only
        num = [str(x) for x in nums]
#         num.sort(cmp=lambda x, y: cmp(y+x, x+y))
        return ''.join(num).lstrip('0') or '0'
    
    def test(self):
        testCases = [
            [3, 30, 34, 5, 9],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.largestNumber(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()