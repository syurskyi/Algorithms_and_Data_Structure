'''
Created on Apr 15, 2018

@author: tongq
'''
class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        mod = 10**9+7
        p3 = -1
        p2 = 0
        p1 = 1
        for _ in range(N):
            cur = (p1*2+p3)%mod
            p3 = p2
            p2 = p1
            p1 = cur
        return p1
    
    def test(self):
        testCases = [
            3,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.numTilings(n)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
