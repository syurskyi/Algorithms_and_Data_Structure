'''
Created on Feb 9, 2017

@author: MT
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s: return []
        dp = [[] for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)+1):
            if dp[i]:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        dp[i+len(word)].append(word)
        res = []
        self.helper(dp, len(s), res, [])
        return res
    
    def helper(self, dp, i, res, curr):
        if i <= 0:
            if i == 0:
                res.append(' '.join(curr))
            return
        for word in dp[i]:
            if i >= len(word):
                curr.insert(0, word)
                self.helper(dp, i-len(word), res, curr)
                curr.pop(0)
    
    def test(self):
        testCases = [
            ('catsanddog', ["cat", "cats", "and", "sand", "dog"]),
        ]
        for s, wordDict in testCases:
            print('s: %s' % (s))
            print('wordDict: %s' % (wordDict))
            result = self.wordBreak(s, wordDict)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
