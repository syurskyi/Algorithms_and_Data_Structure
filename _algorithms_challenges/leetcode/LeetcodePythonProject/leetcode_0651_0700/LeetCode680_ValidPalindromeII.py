'''
Created on Oct 19, 2017

@author: MT
'''
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        i, j = 0, len(s)-1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        if i >= j:
            return True
        i0, j0 = i, j
        i += 1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        if i >= j:
            return True
        i, j = i0, j0
        j -= 1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        if i >= j:
            return True
        return False
    
    def test(self):
        testCases = [
            'aba',
            'abca',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.validPalindrome(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
