'''
Created on Mar 4, 2017

@author: MT
'''

class Solution(object):
    def canPermutePalindrome(self, s):
        if not s: return False
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        odd = 0
        for value in hashmap.values():
            if value%2 != 0:
                odd += 1
        if len(s)%2 == 0:
            return bool(odd == 0)
        else:
            return bool(odd < 2)