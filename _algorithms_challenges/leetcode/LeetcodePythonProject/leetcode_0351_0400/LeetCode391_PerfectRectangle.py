'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object):
    def isRectangleCover(self, rectangles):
        if not rectangles:
            return False
        x1, x2, y1, y2 = float('inf'), float('-inf'), float('inf'), float('-inf')
        hashset = set()
        area = 0
        for rect in rectangles:
            x1 = min(x1, rect[0])
            y1 = min(y1, rect[1])
            x2 = max(x2, rect[2])
            y2 = max(y2, rect[3])
            
            area += (rect[2]-rect[0])*(rect[3]-rect[1])
            
            if (rect[0], rect[1]) not in hashset:
                hashset.add((rect[0], rect[1]))
            else:
                hashset.discard((rect[0], rect[1]))
            if (rect[0], rect[3]) not in hashset:
                hashset.add((rect[0], rect[3]))
            else:
                hashset.discard((rect[0], rect[3]))
            if (rect[2], rect[3]) not in hashset:
                hashset.add((rect[2], rect[3]))
            else:
                hashset.discard((rect[2], rect[3]))
            if (rect[2], rect[1]) not in hashset:
                hashset.add((rect[2], rect[1]))
            else:
                hashset.discard((rect[2], rect[1]))
        
        if (x1, y1) not in hashset or\
            (x1, y2) not in hashset or\
            (x2, y1) not in hashset or\
            (x2, y2) not in hashset or\
            len(hashset) != 4:
            return False
        
        return area == (x2-x1)*(y2-y1)
        
    