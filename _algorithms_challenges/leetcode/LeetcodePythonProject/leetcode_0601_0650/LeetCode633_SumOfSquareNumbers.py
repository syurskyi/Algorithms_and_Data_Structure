'''
Created on Sep 24, 2017

@author: MT
'''

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        if c < 0: return False
        l, r = 0, int(math.sqrt(c))
        while l <= r:
            if l*l + r*r < c:
                l += 1
            elif l*l + r*r > c:
                r -= 1
            else:
                return True
        return False
    
    def test(self):
        testCases = [
            0,
            3,
            4,
            5,
        ]
        for c in testCases:
            print(c)
            result = self.judgeSquareSum(c)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
