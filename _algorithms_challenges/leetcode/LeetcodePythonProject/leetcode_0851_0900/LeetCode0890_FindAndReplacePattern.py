'''
Created on Oct 31, 2019

@author: tongq
'''
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for word in words:
            if self.isSimliar(word, pattern):
                res.append(word)
        return res
    
    def isSimliar(self, w1, w2):
        if len(w1) != len(w2): return False
        hashmap1, hashmap2 = {}, {}
        for c1, c2 in zip(w1, w2):
            if c1 not in hashmap1:
                if c2 in hashmap2:
                    return False
                hashmap1[c1] = c2
                hashmap2[c2] = c1
            else:
                if c2 not in hashmap2:
                    return False
                if hashmap2[c2] != c1 or hashmap1[c1] != c2:
                    return False
        return True
    
    def test(self):
        testCases = [
            [
                ["abc","deq","mee","aqq","dkd","ccc"],
                "abb",
            ],
        ]
        for words, pattern in testCases:
            res = self.findAndReplacePattern(words, pattern)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
