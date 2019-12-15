'''
Created on Apr 8, 2017

@author: MT
'''

class Solution(object):
    def readBinaryWatch(self, num):
        result = []
        for i in range(12):
            for j in range(60):
                total = self.countDigits(i) + self.countDigits(j)
                if total == num:
                    s = '%s:%02d' % (i, j)
                    result.append(s)
        return result
    
    def countDigits(self, num):
        result = 0
        while num > 0:
            if num & 1 == 1:
                result += 1
            num >>= 1
        return result
    