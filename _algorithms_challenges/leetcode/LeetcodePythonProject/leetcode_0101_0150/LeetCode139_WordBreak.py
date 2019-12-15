'''
Created on Feb 9, 2017

@author: MT
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            if not dp[i]:
                continue
            for word in wordDict:
                end = i+len(word)
                sub = s[i:end]
                if sub == word:
                    dp[end] = True
        return dp[-1]
    
    def test(self):
        pass

if __name__ == '__main__':
    Solution().test()