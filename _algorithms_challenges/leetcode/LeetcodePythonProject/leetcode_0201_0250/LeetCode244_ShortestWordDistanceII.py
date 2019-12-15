'''
Created on May 14, 2018

@author: tongq
'''
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        hashmap = {}
        for i, word in enumerate(words):
            hashmap[word] = hashmap.get(word, [])+[i]
        self.hashmap = hashmap
    
    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i, j = 0, 0
        res = float('inf')
        arr1, arr2 = self.hashmap[word1], self.hashmap[word2]
        while i < len(arr1) and j < len(arr2):
            res = min(res, abs(arr1[i]-arr2[j]))
            if arr1[i] > arr2[j]:
                j += 1
            else:
                i += 1
        return res
