'''
Created on Feb 11, 2017

@author: MT
'''
# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        if not points: return 0
        if n <= 2: return n
        res = 0
        for i in range(n):
            hashmap = {}
            dup = 0
            tmpMax = 0
            for j in range(i+1, n):
                x = points[j].x-points[i].x
                y = points[j].y-points[i].y
                if x == 0 and y == 0:
                    dup += 1
                    continue
                gcd = self.gcd(x, y)
                if gcd:
                    x //= gcd
                    y //= gcd
                if x in hashmap:
                    if y in hashmap[x]:
                        hashmap[x][y] += 1
                    else:
                        hashmap[x][y] = 1
                else:
                    hashmap0 = {}
                    hashmap0[y] = 1
                    hashmap[x] = hashmap0
                tmpMax = max(tmpMax, hashmap[x][y])
            res = max(res, tmpMax+dup+1)
        return res
    
    def gcd(self, a, b):
        if b == 0: return a
        return self.gcd(b, a%b)
    
    def maxPoints_slope(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points: return 0
        maxVal = 0
        n = len(points)
        for i in range(n):
            duplicate, vertical = 1, 0
            hashmap = {}
            for j in range(i+1, n):
                if points[i].x == points[j].x:
                    if points[i].y == points[j].y:
                        duplicate += 1
                    else:
                        vertical += 1
                else:
                    if points[j].y == points[i].y:
                        slope = 0.0
                    else:
                        slope = float(points[j].y-points[i].y)/(points[j].x-points[i].x)
                    if slope not in hashmap:
                        hashmap[slope] = 1
                    else:
                        hashmap[slope] += 1
            for count in hashmap.values():
                if count + duplicate > maxVal:
                    maxVal = count + duplicate
            maxVal = max(vertical+duplicate, maxVal)
        return maxVal
    
    def test(self):
        testCases = [
            [[1,1],[2,2],[3,3]],
            [[0,0],[94911151,94911150],[94911152,94911151]],
        ]
        for l in testCases:
            points = [Point(x[0], x[1]) for x in l]
            print('points: %s' % (l))
            result = self.maxPoints(points)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
    