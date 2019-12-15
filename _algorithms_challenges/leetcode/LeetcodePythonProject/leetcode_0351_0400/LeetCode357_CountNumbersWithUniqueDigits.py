'''
Created on Mar 23, 2017

@author: MT
'''

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0: return 1
        res = 10
        uniqueDigits = 9
        availableNumbers = 9
        while n > 1 and availableNumbers > 0:
            uniqueDigits = uniqueDigits*availableNumbers
            res += uniqueDigits
            availableNumbers -= 1
            n -= 1
        return res
