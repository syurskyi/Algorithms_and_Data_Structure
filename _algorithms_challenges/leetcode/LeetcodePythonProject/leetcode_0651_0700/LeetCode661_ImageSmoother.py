'''
Created on Oct 8, 2017

@author: MT
'''
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        import math
        matrix = M
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count = float(matrix[i][j])
                num = 1.0
                for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1),\
                    (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1):
                    if 0 <= x < m and 0 <= y < n:
                        if matrix[x][y] != 0:
                            count += float(matrix[x][y])
                        num += 1
                tmp = int(math.floor(count/num))
                res[i][j] = tmp
        return res
    
    def test(self):
        testCases = [
            [
                [2,3],
            ],
            [
                [1,1,1],
                [1,0,1],
                [1,1,1],
            ],
            [
                [2, 3, 4],
                [5, 6, 7],
                [8, 9, 10],
                [11,12,13],
                [14,15,16],
            ]
        ]
        for matrix in testCases:
            print('matrix:')
            print('\n'.join([str(row) for row in matrix]))
            result = self.imageSmoother(matrix)
            print('result:')
            print('\n'.join([str(row) for row in result]))
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
