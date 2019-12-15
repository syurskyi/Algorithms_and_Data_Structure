'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        for i in range(1, n//2+2):
            sub = s[:i]
            if len(s)%len(sub) == 0:
                j = i
                while j+len(sub) <= n and s[j:j+len(sub)]==sub:
                    j += len(sub)
                    if j == n:
                        return True
        return False
