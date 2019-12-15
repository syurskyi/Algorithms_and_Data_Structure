'''
Created on Feb 18, 2017

@author: MT
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        notPrime = [False]*(n)
        count = 0
        for i in range(2, n):
            if not notPrime[i]:
                count += 1
                j = 2
                while i*j < n:
                    notPrime[i*j] = True
                    j += 1
        return count
    
    def countPrimesSqrt(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        if n <= 2:
            return 0
        primes = [False,]*2 + [True,]*(n-2)
        for i in range(2, int(math.sqrt(n-1))+1):
            if primes[i]:
                for j in range(i+i, n, i):
                    primes[j] = False
        count = 0
        for i in range(2, n):
            if primes[i]: count += 1
        print(primes)
        return count
    
    def test(self):
        testCases = [
            6,
        ]
        for n in testCases:
            print('n: %s' % (n))
            result = self.countPrimes(n)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
