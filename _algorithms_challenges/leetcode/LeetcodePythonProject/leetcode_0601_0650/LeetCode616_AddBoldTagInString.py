'''
Created on Sep 7, 2017

@author: MT
'''
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        dict.sort(key=len, reverse=True)
        n = len(s)
        res = ''
        maxLen = -1
        started = False
        for i in range(n):
            for word in dict:
                if i+len(word) <= n and s[i:i+len(word)] == word:
                    maxLen = max(maxLen, i+len(word))
                    break
            if maxLen > i and not started:
                res += '<b>'+s[i]
                started = True
            elif maxLen == i:
                res += '</b>'+s[i]
                started = False
            else:
                res += s[i]
        if maxLen == len(s):
            res += '</b>'
        return res
    
    def test(self):
        testCases = [
            [
                'abcxyz123',
                ['abc', '123'],
            ],
            [
                'aaabbcc',
                ['aaa', 'aab', 'bc'],
            ],
            [
                'aaabbcc',
                [],
            ],
        ]
        for s, d in testCases:
            print('s: %s' % s)
            print('d: %s' % d)
            result = self.addBoldTag(s, d)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
