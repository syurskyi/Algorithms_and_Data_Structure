'''
Created on Mar 6, 2019

@author: tongq
'''
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """

import collections, itertools

class Master(object):
    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        pass

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        n = 0
        while n < 6:
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if self.match(w1, w2) == 0)
            guess = min(wordlist, key=lambda w:count[w])
            n = master.guess(guess)
            wordlist = [w for w in wordlist if self.match(w, guess) == n]
    
    def match(self, w1, w2):
        matches = 0
        for c1, c2 in zip(w1, w2):
            if c1 == c2: matches += 1
        return matches
    
    def test(self):
        testCases = [
            
        ]
        for wordlist, master in testCases:
            result = self.findSecretWord(wordlist, master)
            print('result: %s' % result)

if __name__ == '__main__':
    Solution().test()
