'''
Created on Jan 31, 2018

@author: tongq
'''
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words: return ''
        words.sort(key=len)
        n = len(words[-1])
        dp = [set() for _ in range(n+1)]
        for word in words:
            if len(word) == 1 or word[:-1] in dp[len(word)-1]:
                dp[len(word)].add(word)
        for i in range(n, -1, -1):
            if dp[i]:
                return sorted(list(dp[i])).pop(0)
        return ''
    
    def test(self):
        testCases = [
            ["w","wo","wor","worl", "world"],
            ["a", "banana", "app", "appl", "ap", "apply", "apple"],
        ]
        for words in testCases:
            print('words: %s' % words)
            result = self.longestWord(words)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
