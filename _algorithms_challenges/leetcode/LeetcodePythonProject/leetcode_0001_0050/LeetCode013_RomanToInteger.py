'''
Created on Nov 7, 2017

@author: MT
'''
class Solution(object):
    def romanToInt(self, s):
        hashmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0
        for i, c in enumerate(s):
            curVal = hashmap[c]
            if i+1 < len(s) and hashmap[s[i+1]] > curVal:
                res -= curVal
            else:
                res += curVal
        return res
