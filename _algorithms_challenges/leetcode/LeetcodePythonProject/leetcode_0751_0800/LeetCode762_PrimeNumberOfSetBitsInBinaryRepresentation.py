'''
Created on Apr 2, 2018

@author: tongq
'''
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = set([2, 3, 5, 7, 11, 13, 17, 19])
        cnt = 0
        for num in range(L, R+1):
            bits = 0
            n = num
            while n > 0:
                bits += n & 1
                n >>= 1
            cnt += 1 if bits in primes else 0
        return cnt
    
    def test(self):
        testCases = [
            [6, 10],
            [10, 15],
            [942063, 945851],
        ]
        for l, r in testCases:
            print('l: %s' % l)
            print('r: %s' % r)
            result = self.countPrimeSetBits(l, r)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
