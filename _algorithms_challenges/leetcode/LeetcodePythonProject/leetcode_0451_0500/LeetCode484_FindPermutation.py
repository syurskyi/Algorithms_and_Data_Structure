'''
Created on May 3, 2017

@author: MT
'''

class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s)
        res = list(range(1, n+2))
        i = 0
        while i < n:
            if s[i] == 'D':
                prev = i
                while i+1 < n and s[i+1]=='D':
                    i += 1
                self.reverse(res, prev, i+1)
            i += 1
        return res
    
    def reverse(self, res, l, r):
        while l < r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
    
    def test(self):
        testCases = [
            'I',
            'DI',
            'DDDI',
            'DIDDI',
            'DD',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.findPermutation(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
