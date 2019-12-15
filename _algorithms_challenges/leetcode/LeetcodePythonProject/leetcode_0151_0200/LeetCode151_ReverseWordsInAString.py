'''
Created on May 22, 2018

@author: tongq
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or not s.strip(): return ''
        return ' '.join([x.strip() for x in s.strip().split(' ') if x][::-1])
