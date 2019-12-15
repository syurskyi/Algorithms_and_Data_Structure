'''
Created on Apr 27, 2017

@author: MT
'''
class Solution():
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i-1) ^ num
    
    def findComplement_another(self, num):
        result = 0
        start = False
        for i in range(31, -1, -1):
            first = (num >> i)&1
            if first == 1 and start == False:
                start = True
            if start:
                if first == 0:
                    result += (1 << i)
        return result
