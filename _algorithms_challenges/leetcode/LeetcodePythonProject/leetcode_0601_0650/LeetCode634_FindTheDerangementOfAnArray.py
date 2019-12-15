'''
Created on Sep 24, 2017

@author: MT
'''
class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        dn1, dn2 = 1, 0
        if n <= 1: return 0
        res = 1
        for i in range(3, n+1):
            res = ((i-1)*(dn1+dn2))%(10**9+7)
            dn2 = dn1
            dn1 = res
        return int(res)
    
    def test(self):
        testCases = [
            1,
            2,
            3,
            4,
            10,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.findDerangement(n)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
