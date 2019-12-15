'''
Created on Apr 18, 2018

@author: tongq
'''
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        s1, s2 = A, B
        if len(s1) != len(s2):
            return False
        if s1 == s2: return True
        for i in range(len(s1)):
            if s1[i:] + s1[:i] == s2:
                return True
        return False
    
    def test(self):
        testCases = [
            ['abcde', 'cdeab'],
            ['abcde', 'abced'],
        ]
        for s1, s2 in testCases:
            print('s1: %s' % s1)
            print('s2: %s' % s2)
            result = self.rotateString(s1, s2)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
