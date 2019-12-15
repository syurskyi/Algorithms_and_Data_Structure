'''
Created on Feb 21, 2017

@author: MT
'''
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        xA1, xA2, yA1, yA2 = A, C, B, D
        xB1, xB2, yB1, yB2 = E, G, F, H
        common = 0
        aArea = (xA2-xA1)*(yA2-yA1)
        bArea = (xB2-xB1)*(yB2-yB1)
        
        if xA1 <= xB1 <= xA2:
            xTmp = min(xB2, xA2)
            if yA1 <= yB1 < yA2:
                yTmp = min(yB2, yA2)
                common = (xTmp-xB1)*(yTmp-yB1)
            elif yB1 <= yA1 < yB2:
                yTmp = min(yA2, yB2)
                common = (xTmp-xB1)*(yTmp-yA1)
        elif xB1 <= xA1 <= xB2:
            xTmp = min(xB2, xA2)
            if yA1 <= yB1 < yA2:
                yTmp = min(yB2, yA2)
                common = (xTmp-xA1)*(yTmp-yB1)
            elif yB1 <= yA1 < yB2:
                yTmp = min(yA2, yB2)
                common = (xTmp-xA1)*(yTmp-yA1)
        return aArea+bArea-common
