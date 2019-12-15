'''
Created on Sep 5, 2017

@author: MT
'''

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        lengths = [
            self.getLen(p1, p2),
            self.getLen(p2, p3),
            self.getLen(p3, p4),
            self.getLen(p4, p1),
            self.getLen(p1, p3),
            self.getLen(p2, p4),
        ]
        maxVal, nonMax = 0, 0
        count = 0
        for length in lengths:
            maxVal = max(maxVal, length)
        for length in lengths:
            if maxVal != length:
                nonMax = length
            else:
                count += 1
        if count != 2: return False
        for length in lengths:
            if nonMax != length and maxVal != length:
                return False
        return True
    
    def getLen(self, p1, p2):
        return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
