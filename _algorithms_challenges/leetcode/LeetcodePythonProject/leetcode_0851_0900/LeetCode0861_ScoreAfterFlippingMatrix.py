'''
Created on Sep 17, 2019

@author: tongq
'''
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        matrix = A
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0 if matrix[i][j] else 1
        for j in range(1, n):
            count = 0
            for i in range(m):
                if matrix[i][j] == 1:
                    count += 1
            if 2*count < m:
                for i in range(m):
                    matrix[i][j] = 0 if matrix[i][j] else 1
        res = 0
        for i in range(m):
            num = 0
            for j in range(n):
                num = num*2 + matrix[i][j]
            res += num
        return res
    
    def test(self):
        testCase = [
#             [
#                 [0,0,1,1],
#                 [1,0,1,0],
#                 [1,1,0,0]
#             ],
            [
                [0,1],
                [1,1]
            ],
        ]
        for matrix in testCase:
            res = self.matrixScore(matrix)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()

