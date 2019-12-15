'''
Created on May 22, 2018

@author: tongq
'''
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        prev = lower
        for num in nums:
            if num == prev+1:
                res.append('%s' % prev)
            elif num > prev+1:
                res.append('%s->%s' % (prev, min(num-1, upper)))
            prev = num+1
            if prev > upper:
                break
        if upper == prev:
            res.append('%s' % prev)
        elif upper > prev:
            res.append('%s->%s' % (prev, upper))
        return res
    
    def test(self):
        testCases = [
            [
                [0,1,3,50,75],
                0, 99,
            ],
        ]
        for nums, lower, upper in testCases:
            print('nums: %s' % nums)
            print('lower: %s' % lower)
            print('upper: %s' % upper)
            result = self.findMissingRanges(nums, lower, upper)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
