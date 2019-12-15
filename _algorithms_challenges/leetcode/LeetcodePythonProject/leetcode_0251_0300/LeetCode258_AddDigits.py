'''
Created on May 13, 2018

@author: tongq
'''
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num-9*((num-1)/9) if num != 0 else 0
    
    def addDigits_slow(self, num):
        while num >= 10:
            newNum = 0
            while num > 0:
                digit = num%10
                num = num//10
                newNum += digit
            num = newNum
        return num
