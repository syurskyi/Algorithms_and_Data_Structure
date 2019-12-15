'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object):
    def lastRemaining(self, n):
        left = True
        remaining = n
        head = 1
        step = 1
        while remaining > 1:
            if left or remaining%2==1:
                head += step
            remaining //= 2
            step *= 2
            left = not left
        return head
    
    def test(self):
        testCases = [
            9
        ]
        for num in testCases:
            print('num: %s' % num)
            result = self.lastRemaining(num)
            print('result1: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
