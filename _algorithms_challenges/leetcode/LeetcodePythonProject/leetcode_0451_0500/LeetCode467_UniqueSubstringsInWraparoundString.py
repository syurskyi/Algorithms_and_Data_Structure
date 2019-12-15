'''
Created on Apr 25, 2017

@author: MT
'''

class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        count = [0]*26
        maxCurrLen = 0
        for i, c in enumerate(p):
            if i > 0 and (ord(c)-ord(p[i-1])==1 or (c=='a' and p[i-1]=='z')):
                maxCurrLen += 1
            else:
                maxCurrLen = 1
            count[ord(c)-ord('a')] = max(count[ord(c)-ord('a')], maxCurrLen)
        return sum(count)
    
    def test(self):
        testCases = [
            'a',
            'cac',
            'zab',
            'zaba',
        ]
        for p in testCases:
            print('p: %s' % p)
            result = self.findSubstringInWraproundString(p)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
