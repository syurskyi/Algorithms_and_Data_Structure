'''
Created on May 25, 2018

@author: tongq
'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordSet = set(wordList)
        wordSet.add(beginWord)
        # DON'T ADD endWord
        visited = set([beginWord])
        queue = [beginWord]
        length = 0
        while queue:
            n = len(queue)
            length += 1
            for _ in range(n):
                word = queue.pop(0)
                if word == endWord:
                    return length
                nextWords = self.getNext(word, wordSet)
                for nextWord in nextWords:
                    if nextWord not in visited:
                        visited.add(nextWord)
                        queue.append(nextWord)
        return 0
    
    def getNext(self, word, wordSet):
        chars = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        for i, c in enumerate(word):
            for c0 in chars:
                if c != c0:
                    word0 = word[:i]+c0+word[i+1:]
                    if word0 in wordSet:
                        res.append(word0)
        return res
    
    def test(self):
        testCases = [
            [
                "hit",
                "cog",
                ["hot","dot","dog","lot","log","cog"],
            ],
            [
                "hit",
                "cog",
                ["hot","dot","dog","lot","log"],
            ],
        ]
        for beginWord, endWord, wordList in testCases:
            result = self.ladderLength(beginWord, endWord, wordList)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
