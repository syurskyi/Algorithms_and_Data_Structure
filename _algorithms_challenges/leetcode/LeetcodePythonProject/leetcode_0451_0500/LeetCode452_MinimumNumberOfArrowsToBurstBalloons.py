'''
Created on Apr 20, 2017

@author: MT
'''

class Solution(object):
    def findMinArrowShots(self, points):
        if not points: return 0
        points.sort(key=lambda x: (x[1], x[0]))
        count = 0
        maxLen = float('-inf')
        for point in points:
            if point[0] > maxLen:
                maxLen = point[1]
            else:
                count += 1
        return len(points)-count
    
    def test(self):
        testCases = [
            [[10,16], [2,8], [1,6], [7,12]],
        ]
        for points in testCases:
            print('points: %s' % points)
            result = self.findMinArrowShots(points)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
