'''
Created on Oct 15, 2017

@author: MT
'''
class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0: return 1
        if n == 1: return 2
        if n == 2 and m == 1: return 3
        if n == 2: return 4
        if m == 1: return 4
        if m == 2: return 7
        if m >= 3: return 8
        return 8
    
    def test(self):
        testCases = [
            [
                1,
                1,
            ],
            [
                2,
                1,
            ],
            [
                3,
                1,
            ],
        ]
        for n, m in testCases:
            print('n: %s' % n)
            print('m: %s' % m)
            result = self.flipLights(n, m)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
