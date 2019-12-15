'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object):
    def hammingDistance(self, x, y):
        count = 0
        for i in range(32):
            count += (x>>i&1)^(y>>i&1)
        return count
    
    def test(self):
        testCases = [
            [1, 4],
        ]
        for x, y in testCases:
            print('x: %s' % x)
            print('y: %s' % y)
            result = self.hammingDistance(x, y)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
