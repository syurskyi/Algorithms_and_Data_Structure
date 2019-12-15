'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0: return []
        result = [[0]*n for i in range(n)]
        left, right, top, down = 0, n-1, 0, n-1
        count = 1
        while left<=right and top<=down:
            for i in range(left, right+1):
                result[top][i] = count
                count+=1
            top += 1
            for i in range(top, down+1):
                result[i][right] = count
                count+=1
            right -= 1
            for i in range(right, left-1, -1):
                result[down][i] = count
                count+=1
            down -= 1
            for i in range(down, top-1, -1):
                result[i][left] = count
                count+=1
            left += 1
        return result
    
    def test(self):
        for n in range(1, 5):
            print('n: %s' % n)
            matrix = self.generateMatrix(n)
            print('matrix: %s' % matrix)
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()