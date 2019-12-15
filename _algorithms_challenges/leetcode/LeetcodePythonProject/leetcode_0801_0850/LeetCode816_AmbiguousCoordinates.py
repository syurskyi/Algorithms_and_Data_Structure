'''
Created on May 1, 2018

@author: tongq
'''
class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        s = S
        n = len(s)
        res = []
        for i in range(1, n-2):
            arrA = self.helper(s[1:i+1])
            arrB = self.helper(s[i+1:n-1])
            for s1 in arrA:
                for s2 in arrB:
                    res.append('(%s, %s)' % (s1, s2))
        return res
    
    def helper(self, s):
        n = len(s)
        res = []
        if n == 0 or (n > 1 and s[0] == '0' and s[-1] == '0'):
            return res
        if n > 1 and s[0] == '0':
            res.append('0.'+s[1:])
            return res
        res.append(s)
        if n == 1 or s[-1] == '0':
            return res
        for i in range(1, n):
            res.append(s[:i]+'.'+s[i:])
        return res
    
    def test(self):
        testCases = [
            '(123)',
            '(00011)',
            '(0123)',
            '(100)',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.ambiguousCoordinates(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
