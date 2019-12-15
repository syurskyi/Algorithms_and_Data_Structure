'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        result = []
        
        top, down, left, right = 0, m-1, 0, n-1
        
        while top <= down and left <= right:
            if top == down:
                for i in range(left, right+1):
                    result.append(matrix[top][i])
                break
              
            if left == right:
                for i in range(top, down+1):
                    result.append(matrix[i][left])
                break
                
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, down+1):
                result.append(matrix[i][right])
            right-=1
            for i in range(right, left-1, -1):
                result.append(matrix[down][i])
            down-=1
            for i in range(down, top-1, -1):
                result.append(matrix[i][left])
            left+=1
        
        return result
    
    def test(self):
        matrixes = [
            [
                [ 1, 2, 3 ],
                [ 4, 5, 6 ],
                [ 7, 8, 9 ],
            ],
            [
                [1, 2, 3, 4],
            ],
            [
                [1, 2],
                [3, 4],
                [5, 6],
            ],
            [
                [1],
                [2],
                [3],
                [4],
            ],
            [
                [1, 2],
                [3, 4],
            ],
        ]
        
        for matrix in matrixes:
            print(matrix)
            result = self.spiralOrder(matrix)
            print(result)
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()