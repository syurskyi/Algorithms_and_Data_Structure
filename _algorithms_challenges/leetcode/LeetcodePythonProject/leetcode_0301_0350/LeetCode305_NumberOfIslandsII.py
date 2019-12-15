'''
Created on Mar 11, 2017

@author: MT
'''
class Solution(object):
    def numIslands2(self, m, n, positions):
        res = []
        roots = [-1]*(m*n)
        grid = [[False]*n for _ in range(m)]
        count = 0
        for pos in positions:
            i, j = pos[0], pos[1]
            grid[i][j] = True
            count += 1
            root0 = i*n+j
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    root = self.getRoot(roots, x*n+y)
                    if root != root0:
                        count -= 1
                        roots[root] = root0
            res.append(count)
        return res
    
    def getRoot(self, roots, ind):
        while roots[ind] != -1:
            ind = roots[ind]
        return ind
    
    def test(self):
        testCases = [
            (3, 3, [[0,0], [0,1], [1,2], [2,1]]),
            [
                3,
                3,
                [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]],
            ],
            [
                8,
                4,
                [[0,0],[7,1],[6,1],[3,3],[4,1]],
            ],
        ]
        for m, n, positions in testCases:
            print('m: %s' % (m))
            print('n: %s' % (n))
            print('positions: %s' % (positions))
            result = self.numIslands2(m, n, positions)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
