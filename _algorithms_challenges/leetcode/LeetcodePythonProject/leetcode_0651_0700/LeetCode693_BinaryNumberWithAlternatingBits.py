'''
Created on Oct 25, 2017

@author: MT
'''
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = n&1
        n >>= 1
        while n > 0:
            digit = n & 1
            if not digit ^ prev:
                return False
            prev = digit
            n >>= 1
        return True
    
    def test(self):
        testCases = [
            4,
            5,
            7,
            11,
            10,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.hasAlternatingBits(n)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
