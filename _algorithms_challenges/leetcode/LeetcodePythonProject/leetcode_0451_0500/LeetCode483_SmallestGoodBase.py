'''
Created on May 3, 2017

@author: MT
'''

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        import math
        n = int(n)
        max_n = int(math.log(n, 2))
        for m in range(max_n, 1, -1):
            k = int(n**m**-1)
            if (k**(m+1)-1)//(k-1) == n:
                return str(k)
        return str(n-1)
    
    def test(self):
        testCases = [
            '13',
            '4681',
            '1000000000000000000',
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.smallestGoodBase(n)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
