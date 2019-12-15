'''
Created on Feb 27, 2017

@author: MT
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t: return True
        if not s or not t: return False
        if len(s) != len(t): return False
        hashmap = {}
        for c in s:
            if c in hashmap: hashmap[c] += 1
            else: hashmap[c] = 1
        for c in t:
            if c not in hashmap: return False
            hashmap[c] -= 1
            if hashmap[c] == 0:
                del hashmap[c]
        if hashmap:
            return False
        return True
    
    