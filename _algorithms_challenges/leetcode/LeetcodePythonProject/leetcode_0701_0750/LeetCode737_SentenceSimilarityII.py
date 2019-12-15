'''
Created on Mar 13, 2018

@author: tongq
'''
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        pairInfo = {}
        for p in pairs:
            if p[0] not in pairInfo:
                pairInfo[p[0]] = set()
            if p[1] not in pairInfo:
                pairInfo[p[1]] = set()
            pairInfo[p[0]].add(p[1])
            pairInfo[p[1]].add(p[0])
        for w1, w2 in zip(words1, words2):
            if w1 == w2:
                continue
            if w1 not in pairInfo:
                return False
            if not self.dfs(w1, w2, pairInfo, set()):
                return False
        return True
    
    def dfs(self, source, target, pairInfo, visited):
        if target in pairInfo.get(source, set()):
            return True
        visited.add(source)
        for nextWord in pairInfo.get(source, set()):
            if nextWord not in visited and self.dfs(nextWord, target, pairInfo, visited):
                return True
        return False
    
    # This is Exceeding Time Limit
    def areSentencesSimilarTwo_own(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        hashmap = {}
        n = 0
        l = []
        for p in pairs:
            if p[0] not in hashmap:
                l.append(p[0])
                hashmap[p[0]] = n
                n += 1
            if p[1] not in hashmap:
                l.append(p[1])
                hashmap[p[1]] = n
                n += 1
        roots = [-1]*n
        for p in pairs:
            root0 = self.getRoot(roots, hashmap[p[0]])
            root1 = self.getRoot(roots, hashmap[p[1]])
            roots[root0] = root1
        for w1, w2 in zip(words1, words2):
            if w1 == w2:
                continue
            elif w1 not in hashmap or w2 not in hashmap:
                return False
            else:
                r1 = self.getRoot(roots, hashmap[w1])
                r2 = self.getRoot(roots, hashmap[w2])
                if r1 != r2:
                    return False
        return True
    
    def getRoot(self, roots, ind):
        while roots[ind] != -1:
            ind = roots[ind]
        return ind
    
    def test(self):
        testCases = [
            [
                ["great", "acting", "skills"],
                ["fine", "drama", "talent"],
                [
                    ["great",   "good"],
                    ["fine",    "good"],
                    ["acting",  "drama"],
                    ["skills",  "talent"],
                ],
            ],
            [
                ["an","extraordinary","meal","meal"],
                ["one","good","dinner"],
                [
                    ["great","good"],
                    ["extraordinary","good"],
                    ["well","good"],
                    ["wonderful","good"],
                    ["excellent","good"],
                    ["fine","good"],
                    ["nice","good"],
                    ["any","one"],
                    ["some","one"],
                    ["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]],
            ],
        ]
        for words1, words2, pairs in testCases:
            result = self.areSentencesSimilarTwo(words1, words2, pairs)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
