'''
Created on May 17, 2018

@author: tongq
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        left = 0
        i = 0
        while i < len(s):
            if s[i] == ' ':
                self.reverse(s, left, i-1)
                left = i+1
            i += 1
        self.reverse(s, left, len(s)-1)
        self.reverse(s, 0, len(s)-1)
    
    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
