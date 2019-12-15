'''
Created on Nov 2, 2017

@author: MT
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle or not needle: return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] == needle[j]:
                    if j == len(needle)-1:
                        return i
                else:
                    break
        return -1
