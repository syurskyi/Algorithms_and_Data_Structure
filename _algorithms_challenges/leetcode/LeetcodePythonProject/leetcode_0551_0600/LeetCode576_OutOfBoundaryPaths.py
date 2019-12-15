'''
Created on Sep 4, 2017

@author: MT
'''
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if N < 0: return 0
        mod = 10**9+7
        count = [[0]*n for _ in range(m)]
        count[i][j] = 1
        result = 0
        for _ in range(N):
            tmp = [[0]*n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                        if 0 <= nr < m and 0 <= nc < n:
                            tmp[nr][nc] = (tmp[nr][nc]+count[r][c])%mod
                        else:
                            result = (result+count[r][c])%mod
            count = tmp
        return result
    
    def test(self):
        testCases = [
            [2, 2, 2, 0, 0],
            [1, 3, 3, 0, 1],
        ]
        for m, n, N, i, j in testCases:
            print('m: %s' % m)
            print('n: %s' % n)
            print('N: %s' % N)
            print('i: %s' % i)
            print('j: %s' % j)
            result = self.findPaths(m, n, N, i, j)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
