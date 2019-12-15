'''
Created on Mar 15, 2017

@author: MT
'''

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        times = [0]*len(primes)
        res = [1]
        for _ in range(n-1):
            minVal = float('inf')
            for i, p in zip(times, primes):
                minVal = min(minVal, res[i]*p)
            res.append(minVal)
            for i in range(len(times)):
                if minVal == res[times[i]]*primes[i]:
                    times[i] += 1
        return res[-1]
