'''
Created on Oct 22, 2017

@author: MT
'''
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        s1, s2 = A, B
        n1, n2 = len(s1), len(s2)
        k = n2//n1+2
        if str(s1*k).count(s2)==0:
            return -1
        while k >= 1 and str(s1*k).count(s2)!=0:
            k -= 1
        return k+1
    
    def test(self):
        testCases = [
            [
                'abcd',
                'cdabcdab',
            ]
        ]
        for A, B in testCases:
            print('A: %s' % A)
            print('B: %s' % B)
            result = self.repeatedStringMatch(A, B)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
