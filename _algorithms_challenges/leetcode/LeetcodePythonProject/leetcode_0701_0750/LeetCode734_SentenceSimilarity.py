'''
Created on Mar 7, 2018

@author: tongq
'''
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        hashmap = {}
        for w1, w2 in pairs:
            if w1 not in hashmap:
                hashmap[w1] = set()
            if w2 not in hashmap:
                hashmap[w2] = set()
            hashmap[w1].add(w2)
            hashmap[w2].add(w1)
        if len(words1) != len(words2):
            return False
        for w1, w2 in zip(words1, words2):
            if w1 != w2 and (w1 not in hashmap or w2 not in hashmap[w1]):
                return False
        return True
    
    def test(self):
        testCases = [
            [
                ["a","very","delicious","meal"],
                ["one","really","good","dinner"],
                [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]],
            ],
            [
                ['great', 'acting', 'skills'],
                ['fine', 'drama', 'talent'],
                [["great", "fine"], ["acting","drama"], ["skills","talent"]],
            ],
        ]
        for words1, words2, pairs in testCases:
            print('words1: %s' % words1)
            print('words2: %s' % words2)
            print('pairs: %s' % pairs)
            result = self.areSentencesSimilar(words1, words2, pairs)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
