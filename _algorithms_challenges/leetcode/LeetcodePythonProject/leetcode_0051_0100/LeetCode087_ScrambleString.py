'''
Created on May 31, 2018

@author: tongq
'''
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        if len(s1) == 0 or s1 == s2:
            return True
        l1 = list(s1)
        l2 = list(s2)
        l1.sort()
        l2.sort()
        if l1 != l2:
            return False
        for i in range(1, len(s1)):
            s11 = s1[0:i]
            s12 = s1[i:len(s1)]
            s21 = s2[0:i]
            s22 = s2[i:len(s2)]
            s23 = s2[0:len(s2)-i]
            s24 = s2[len(s2)-i:len(s2)]
            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return True
            if self.isScramble(s11, s24) and self.isScramble(s12, s23):
                return True
        return False
