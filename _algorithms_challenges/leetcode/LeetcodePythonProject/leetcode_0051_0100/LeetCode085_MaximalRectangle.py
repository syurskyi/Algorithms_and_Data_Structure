'''
Created on Jan 25, 2017

@author: MT
'''
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        area = 0
        if not matrix or not matrix[0]: return area
        m, n = len(matrix), len(matrix[0])
        heights = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    heights[i+1][j] = 0
                else:
                    heights[i+1][j] = heights[i][j]+1
        for i in range(m):
            area = max(area, self.getArea(heights[i+1]))
        return area
    
    def getArea(self, heights):
        area = 0
        if not heights: return area
        stack = []
        i = 0
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                h = heights[stack.pop()]
                w = i if not stack else i-stack[-1]-1
                area = max(area, h*w)
        return area
    
    def test(self):
        testCases = [
            [
                ["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"]
            ],
        ]
        for matrix in testCases:
            result = self.maximalRectangle(matrix)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
