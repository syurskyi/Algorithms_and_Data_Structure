'''
Created on Apr 17, 2017

@author: MT
'''

class Solution(object):
    def findKthNumber(self, n, k):
        curr = 1
        k -= 1
        while k > 0:
            steps = self.calSteps(n, curr, curr+1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        return curr
    
    def calSteps(self, n, n1, n2):
        steps = 0
        while n1 <= n:
            steps += min(n+1, n2)-n1
            n1 *= 10
            n2 *= 10
        return steps
    
    def test(self):
        testCases = [
            [
                13,
                2,
            ],
        ]
        for n, k in testCases:
            print('n: %s' % n)
            print('k: %s' % k)
            result = self.findKthNumber(n, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
