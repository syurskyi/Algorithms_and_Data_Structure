'''
Created on Mar 29, 2017

@author: MT
'''

class Solution(object):
    def superPow(self, a, b):
        if a % 1337 == 0: return a
        p = 0
        for i in b:
            p = (p*10+i)%1140
        if p == 0:
            p += 1440
        return self.power(a, p, 1337)
    
    def power(self, a, n, mod):
        a %= mod
        res = 1
        while n != 0:
            if ((n&1) != 0):
                res = res*a % mod
            a = a*a%mod
            n >>= 1
        return res
    
    def test(self):
        testCases = [
            [2, [3]],
            [2, [1, 0]],
        ]
        for a, b in testCases:
            print('a: %s' % a)
            print('b: %s' % b)
            result = self.superPow(a, b)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
