'''
Created on May 29, 2018

@author: tongq
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(rowIndex):
            newRes = []
            for j in range(i+2):
                if j == 0 or j == i+1:
                    newRes.append(1)
                else:
                    newRes.append(res[j-1]+res[j])
            res = newRes
        return res
