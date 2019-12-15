'''
Created on Nov 7, 2017

@author: MT
'''
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        nums =  [1000, 900,  500, 400,  100, 90,   50,  40,   10,  9,    5,   4,    1]
        chars = ['M',  'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        for c, n in zip(chars, nums):
            times = num//n
            if times:
                res += c*times
                num -= n*times
        return res
