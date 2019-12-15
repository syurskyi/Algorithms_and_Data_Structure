'''
Created on Oct 16, 2019

@author: tongq
'''
class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        res = []
        dx, dy, n = 0, 1, 0
        while len(res) < R*C:
            for _ in range(n//2+1):
                if 0 <= r0 < R and 0 <= c0 < C:
                    res.append([r0, c0])
                r0, c0 = r0+dx, c0+dy
            dx, dy, n = dy, -dx, n+1
        return res
    
    def spiralMatrixIII_own(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        pos = [r0, c0]
        res = []
        length = 1
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        i = 0
        while len(res) < R*C:
            for _ in range(2):
                for _ in range(length):
                    if self.isInRange(pos, R, C):
                        res.append(pos)
                    d = dirs[i%4]
                    pos = [pos[0]+d[0], pos[1]+d[1]]
                i += 1
            length += 1
        return res
    
    def isInRange(self, pos, R, C):
        return 0 <= pos[0] < R and 0 <= pos[1] < C
    
    def test(self):
        testCases = [
            [1, 4, 0, 0],
        ]
        for R, C, r0, c0 in testCases:
            res = self.spiralMatrixIII(R, C, r0, c0)
            print('res: %s' % res)

if __name__ == '__main__':
    Solution().test()
