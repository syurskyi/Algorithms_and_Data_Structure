'''
Created on Apr 11, 2017

@author: MT
'''

class Solution(object):
    def addStrings(self, num1, num2):
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        i, j = len(num1)-1, len(num2)-1
        result = ''
        carry = 0
        while j >= 0:
            n1 = int(num1[i])
            n2 = int(num2[j])
            val = n1+n2+carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            result = str(val) + result
            i -= 1
            j -= 1
        while i >= 0:
            n1 = int(num1[i])
            val = n1+carry
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            result = str(val) + result
            i -= 1
        if carry:
            result = '1'+result
        return result
