'''
Created on May 1, 2018

@author: tongq
'''
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        hashmap = {}
        res = ''
        freq = 0
        banned = set(banned)
        i = 0
        for j in range(len(paragraph)):
            c = paragraph[j]
            if not (ord('a') <= ord(c) <= ord('z') or\
                ord('A') <= ord(c) <= ord('Z')):
                word = paragraph[i:j].lower()
                if word and word not in banned:
                    hashmap[word] = hashmap.get(word, 0)+1
                    if hashmap[word] > freq:
                        res = word
                        freq = hashmap[word]
                i = j+1
        word = paragraph[i:].lower()
        if word and word not in banned:
            hashmap[word] = hashmap.get(word, 0)+1
            if hashmap[word] > freq:
                res = word
                freq = hashmap[word]
        return res
