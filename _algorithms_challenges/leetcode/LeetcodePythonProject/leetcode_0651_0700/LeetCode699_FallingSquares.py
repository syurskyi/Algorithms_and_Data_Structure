'''
Created on Oct 26, 2017

@author: MT
'''
class Interval(object):
    def __init__(self, start, end, height):
        self.start = start
        self.end = end
        self.height = height

class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res = []
        intervals = []
        h = 0
        for pos in positions:
            cur = Interval(pos[0], pos[0]+pos[1], pos[1])
            h = max(h, self.getHeight(intervals, cur))
            res.append(h)
        return res
    
    def getHeight(self, intervals, cur):
        preMaxHeight = 0
        for i in intervals:
            if i.end <= cur.start: continue
            if i.start >= cur.end: continue
            preMaxHeight = max(preMaxHeight, i.height)
        cur.height += preMaxHeight
        intervals.append(cur)
        return cur.height
    
    def test(self):
        testCases = [
            [[1, 2], [2, 3], [6, 1]],
            [[100, 100], [200, 100]],
            [[6, 1], [9, 2], [2, 4]],
        ]
        for positions in testCases:
            print('positions: %s' % positions)
            result = self.fallingSquares(positions)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
