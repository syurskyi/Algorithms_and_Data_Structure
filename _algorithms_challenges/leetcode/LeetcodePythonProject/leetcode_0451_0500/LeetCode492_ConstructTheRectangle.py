'''
Created on May 8, 2017

@author: MT
'''

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        l = int(math.sqrt(area))
        while l < area:
            if area%l == 0:
                return [max(l, area/l), min(l, area/l)]
            else:
                l += 1
        return [area, 1]
