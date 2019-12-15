'''
Created on Jan 7, 2017

@author: MT
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        div = 1
        while x//div >= 10:
            div *= 10
        while x > 0:
            first = x//div
            last  = x%10
            if first != last:
                return False
            x -= first*div
            x = (x-last)//10
            div //= 100
        return True
    
    def test(self):
        testCases = [
            123,
            121,
            1,
            223322,
            2442,
            24423,
            2453,
            100021,
        ]
        for x in testCases:
            print('x: %s' % (x))
            result = self.isPalindrome(x)
            print('result: %s' % (result))
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
