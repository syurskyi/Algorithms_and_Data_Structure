'''
Created on Oct 8, 2018

@author: tongq
'''
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2
        return x11 < x22 and x21 < x12 and y11 < y22 and y21 < y12
    
    def isRectangleOverlap_own(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2
        if (x11 <= x21 < x12 and (y11 <= y21 < y12 or y21 <= y11 < y12 <= y22)) or\
           (x11 <= x21 < x12 and (y11 < y22 <= y12 or y21 <= y11 < y12 <= y22)) or\
           (x11 < x22 <= x12 and (y11 <= y21 < y12 or y21 <= y11 < y12 <= y22)) or\
           (x11 < x22 <= x12 and (y11 < y22 <= y12 or y21 <= y11 < y12 <= y22)) or\
           (x21 <= x11 < x22 and (y21 <= y11 < y22 or y11 <= y21 < y22 <= y12)) or\
           (x21 <= x11 < x22 and (y21 < y12 <= y22 or y11 <= y21 < y22 <= y12)) or\
           (x21 < x12 <= x22 and (y21 <= y11 < y22 or y11 <= y21 < y22 <= y12)) or\
           (x21 < x12 <= x22 and (y21 < y12 <= y22 or y11 <= y21 < y22 <= y12)):
            return True
        return False

    def test(self):
        testCases = [
            [
                [229,-132,833,333],
                [-244,-577,837,804],
            ],
            [
                [0,0,1,1],
                [1,0,2,1],
            ],
            [
                [7,8,13,15],
                [10,8,12,20],
            ],
        ]
        for rec1, rec2 in testCases:
            result = self.isRectangleOverlap(rec1, rec2)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
