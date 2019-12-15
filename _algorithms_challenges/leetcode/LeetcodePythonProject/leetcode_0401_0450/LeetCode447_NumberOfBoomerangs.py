'''
Created on Apr 18, 2017

@author: MT
'''

class Solution(object):
    def numberOfBoomerangs(self, points):
        n = len(points)
        res = 0
        for i in range(n):
            hashmap = {}
            point1 = points[i]
            for j in range(n):
                point2 = points[j]
                diff = (point2[1]-point1[1])**2+(point2[0]-point1[0])**2
                hashmap[diff] = hashmap.get(diff, 0)+1
            for val in hashmap.values():
                res += val*(val-1)
        return res
    
    def test(self):
        testCases = [
            [[0,0],[1,0],[2,0]],
        ]
        for points in testCases:
            print('points: %s' % points)
            result = self.numberOfBoomerangs(points)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
