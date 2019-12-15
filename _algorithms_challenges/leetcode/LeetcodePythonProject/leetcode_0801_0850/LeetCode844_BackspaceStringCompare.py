'''
Created on Mar 18, 2019

@author: tongq
'''
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s, t = S, T
        s0, t0 = '', ''
        for c in s:
            if c == '#':
                s0 = s0[:-1]
            else:
                s0 += c
        for c in t:
            if c == '#':
                t0 = t0[:-1]
            else:
                t0 += c
        return s0 == t0
    
    def test(self):
        testCases = [
            
        ]
        for s, t in testCases:
            result = self.backspaceCompare(s, t)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
