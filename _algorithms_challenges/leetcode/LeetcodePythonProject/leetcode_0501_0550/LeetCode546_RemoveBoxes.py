'''
Created on Aug 20, 2017

@author: MT
'''

class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        if not boxes: return 0
        n = len(boxes)
        dp = [[[0]*n for _ in range(n)] for _ in range(n)]
        return self.helper(dp, boxes, 0, n-1, 1)
    
    def helper(self, dp, boxes, i, j, k):
        if i > j:
            return 0
        elif i == j:
            return k*k
        elif dp[i][j][k] != 0:
            return dp[i][j][k]
        else:
            tmp = self.helper(dp, boxes, i+1, j, 1) + k*k
            for m in range(i+1, j+1):
                if boxes[i] == boxes[m]:
                    tmp = max(tmp, self.helper(dp, boxes, i+1, m-1, 1)+\
                              self.helper(dp, boxes, m, j, k+1))
            dp[i][j][k] = tmp
            return tmp
    
    def test(self):
        testCases = [
            [1, 3, 2, 2, 2, 3, 4, 3, 1],
        ]
        for boxes in testCases:
            print('boxes: %s' % boxes)
            result = self.removeBoxes(boxes)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
