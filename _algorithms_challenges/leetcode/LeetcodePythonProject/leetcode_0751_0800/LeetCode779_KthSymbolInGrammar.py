'''
Created on Apr 8, 2018

@author: tongq
'''
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return 0
        if K%2 == 0:
            prev = self.kthGrammar(N-1, K/2)
            return 1 if prev == 0 else 0
        else:
            prev = self.kthGrammar(N-1, (K+1)/2)
            return 0 if prev == 0 else 1
    
    def test(self):
        testCases = [
            [1, 1],
            [2, 1],
            [2, 2],
            [4, 5],
            [30, 434991989],
        ]
        for n, k in testCases:
            print('n: %s' % n)
            print('k: %s' % k)
            result = self.kthGrammar(n, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
