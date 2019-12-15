'''
Created on May 24, 2018

@author: tongq
'''
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        wordSet.add(beginWord)
        distance = {}
        self.bfs(beginWord, endWord, distance, wordSet)
        res = []
        self.dfs(beginWord, endWord, distance, wordSet, res, [])
        return res
    
    def bfs(self, beginWord, endWord, distance, wordSet):
        queue = [beginWord]
        distance[beginWord] = 0
        while queue:
            word = queue.pop(0)
            nextWords = self.getNextWords(word, wordSet)
            for nextWord in nextWords:
                if nextWord not in distance:
                    distance[nextWord] = distance[word]+1
                    queue.append(nextWord)
    
    def dfs(self, beginWord, word, distance, wordSet, res, curr):
        curr.insert(0, word)
        if word == beginWord:
            res.append(list(curr))
        else:
            for nextWord in self.getNextWords(word, wordSet):
                if nextWord in distance and distance[nextWord]+1 == distance.get(word, 0):
                    self.dfs(beginWord, nextWord, distance, wordSet, res, curr)
        curr.pop(0)
    
    def getNextWords(self, word, wordSet):
        res = []
        for i, c in enumerate(word):
            for c0 in 'abcdefghijklmnopqrstuvwxyz':
                if c0 != c:
                    word0 = word[:i] + c0 + word[i+1:]
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
        ]
        for beginWord, endWord, wordList in testCases:
            result = self.findLadders(beginWord, endWord, wordList)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
