'''
Created on Apr 10, 2017

@author: MT
'''

class Solution(object):
    def longestPalindrome(self, s):
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        singleNum = False
        result = 0
        for count in hashmap.values():
            if count%2 != 0:
                if singleNum:
                    result += count-1
                else:
                    result += count
                    singleNum = True
            else:
                result += count
        return result
