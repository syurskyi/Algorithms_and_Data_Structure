'''
Created on Oct 8, 2017

@author: MT
'''
class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = ''
        while n:
            res = str(n%9) + res
            n //= 9
        return int(res)
    
    def test(self):
        testCases = [
            9,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.newInteger(n)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
