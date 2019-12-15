'''
Created on Sep 3, 2017

@author: MT
'''
class Solution(object):
    # Don't need extra space if using maxDiff
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        sumVal, maxDiff = 0, float('-inf')
        for nut in nuts:
            dist = abs(tree[0]-nut[0])+abs(tree[1]-nut[1])
            sumVal += dist*2
            maxDiff = max(maxDiff, dist-abs(squirrel[0]-nut[0])-abs(squirrel[1]-nut[1]))
        return sumVal-maxDiff
    
    def minDistance_space(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        n = len(nuts)
        nutToTree = [0]*n
        nutToSquirrel = [0]*n
        sumVal = 0
        for i in range(n):
            nutToTree[i] = abs(nuts[i][0]-tree[0])+abs(nuts[i][1]-tree[1])
            sumVal += nutToTree[i]*2
            nutToSquirrel[i] = abs(nuts[i][0]-squirrel[0])+abs(nuts[i][1]-squirrel[1])
        minVal = float('inf')
        for i in range(n):
            dist = sumVal + nutToSquirrel[i]-nutToTree[i]
            minVal = min(minVal, dist)
        return minVal
    
    def test(self):
        testCases = [
            [
                5,
                7,
                [2, 2],
                [4, 4],
                [[3, 0], [2, 5]],
            ],
            [
                5,
                5,
                [3,2],
                [0,1],
                [[2,0],[4,1],[0,4],[1,3],[1,0],[3,4],[3,0],[2,3],[0,2],[0,0],[2,2],[4,2],[3,3],[4,4],[4,0],[4,3],[3,1],[2,1],[1,4],[2,4]],
            ],
        ]
        for height, width, tree, squirrel, nuts in testCases:
            result = self.minDistance(height, width, tree, squirrel, nuts)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
