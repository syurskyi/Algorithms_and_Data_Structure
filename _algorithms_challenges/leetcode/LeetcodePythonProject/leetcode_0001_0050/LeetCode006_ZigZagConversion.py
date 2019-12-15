'''
Created on Jun 7, 2018

@author: tongq
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or len(s) <= 1 or numRows == 1:
            return s
        step = 2*numRows-2
        res = ''
        for i in range(numRows):
            for j in range(i, len(s), step):
                res += s[j]
                if i != 0 and i != numRows-1 and j+step-2*i < len(s):
                    res += s[j+step-2*i]
        return res
