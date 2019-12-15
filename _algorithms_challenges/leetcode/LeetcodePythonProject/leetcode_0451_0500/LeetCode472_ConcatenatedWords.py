'''
Created on Apr 26, 2017

@author: MT
'''

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        words.sort(key=len)
        hashset = set()
        for word in words:
            if self.helper(hashset, word):
                res.append(word)
            hashset.add(word)
        return res
    
    def helper(self, hashset, word1):
        if not hashset: return False
        dp = [False]*(len(word1)+1)
        dp[0] = True
        for i in range(1, len(word1)+1):
            for j in range(i):
                if dp[j]:
                    if word1[j:i] in hashset:
                        dp[i] = True
                        break
        return dp[-1]
    
    def test(self):
        testCases =[
            [''],
            ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"],
        ]
        for words in testCases:
            print('words: %s' % words)
            result = self.findAllConcatenatedWordsInADict(words)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
