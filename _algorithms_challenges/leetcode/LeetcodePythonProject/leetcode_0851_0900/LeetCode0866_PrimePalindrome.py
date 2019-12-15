'''
Created on Sep 30, 2019

@author: tongq
'''
class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = N
        if 8 <= n <= 11:
            return 11
        for x in range(10**(len(str(n))//2), 10**5):
            y = int(str(x) + str(x)[-2::-1])
            if y >= n and self.isPrime(y):
                return y
    
    def isPrime(self, n):
        if n < 2 or n % 2 == 0:
            return n == 2
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True
    
    def test(self):
        testCases = [
            
        ]
        for n in testCases:
            res = self.primePalindrome(n)
            print('res: %s' % res)

if __name__ == '__main__':
    Solution().test()
