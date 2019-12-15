'''
Created on Mar 30, 2018

@author: tongq
'''
class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        s = S
        words = set(words)
        start = False
        j = 0
        res = ''
        for i in range(len(s)):
            for word in words:
                if i+len(word) <= len(s) and s[i:i+len(word)] == word:
                    if not start:
                        res += '<b>'
                        start = True
                    j = max(j, i+len(word))
            if i == j and start:
                res += '</b>'
                start = False
            res += s[i]
        if j >= len(s):
            res += '</b>'
        return res
    
    def test(self):
        testCases = [
            [
                ['ab', 'bc'],
                'aabcd',
            ],
            [
                ["ccb","b","d","cba","dc"],
                "eeaadadadc",
            ],
            [
                ["b","dee","a","ee","c"],
                "cebcecceab",
            ],
        ]
        for words, s in testCases:
            print('words: %s' % words)
            print('s: %s' % s)
            result = self.boldWords(words, s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
