'''
Created on Apr 29, 2018

@author: tongq
'''
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = 0
        n = len(points)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    res = max(res, self.getArea(points[i], points[j], points[k]))
        return res
    
    def getArea(self, p1, p2, p3):
        return 0.5*abs(p1[0]*p2[1] \
                       +p2[0]*p3[1] \
                       +p3[0]*p1[1] \
                       -p2[0]*p1[1] \
                       -p3[0]*p2[1] \
                       -p1[0]*p3[1])
    
    def test(self):
        testCases = [
            [[0,0],[0,1],[1,0],[0,2],[2,0]],
            [[4,6],[6,5],[3,1]],
        ]
        for points in testCases:
            print('points: %s' % points)
            result = self.largestTriangleArea(points)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
