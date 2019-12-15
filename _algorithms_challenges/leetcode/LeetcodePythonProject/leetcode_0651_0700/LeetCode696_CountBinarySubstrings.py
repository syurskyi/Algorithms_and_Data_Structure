'''
Created on Oct 25, 2017

@author: MT
'''
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        res = 0
        i = 0
        ind = i
        while i+1 < len(s) and s[i+1] == s[ind]:
            i += 1
        prev = i+1-ind
        i += 1
        while i < len(s):
            ind = i
            while i+1 < len(s) and s[i+1] == s[ind]:
                i += 1
            curr = i+1-ind
            res += min(curr, prev)
            prev = curr
            i += 1
        return res
    
    def test(self):
        testCases = [
#             '00110011',
#             '10101',
            "00100",
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.countBinarySubstrings(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
