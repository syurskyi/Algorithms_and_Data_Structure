'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hashmap = {}
        for c in magazine:
            hashmap[c] = hashmap.get(c, 0)+1
        for c in ransomNote:
            if c not in hashmap:
                return False
            hashmap[c] -= 1
            if hashmap[c] == 0:
                del hashmap[c]
        return True
