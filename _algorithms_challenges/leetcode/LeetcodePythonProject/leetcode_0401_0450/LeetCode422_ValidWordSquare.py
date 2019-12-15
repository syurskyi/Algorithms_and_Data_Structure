'''
Created on Apr 13, 2017

@author: MT
'''

class Solution(object):
    def validWordSquare(self, words):
        if not words: return False
        for i, word1 in enumerate(words):
            word2 = ''
            for j in range(len(word1)):
                if j >= len(words):
                    return False
                if i >= len(words[j]):
                    return False
                word2 += words[j][i]
            if word1 != word2:
                return False
        return True
