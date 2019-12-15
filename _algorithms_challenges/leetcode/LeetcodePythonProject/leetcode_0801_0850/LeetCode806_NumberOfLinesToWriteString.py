'''
Created on Apr 24, 2018

@author: tongq
'''
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        s = S
        res = [1, 0]
        for c in s:
            if res[1] + widths[ord(c)-ord('a')] <= 100:
                res[1] += widths[ord(c)-ord('a')]
            else:
                res[0] += 1
                res[1] = widths[ord(c)-ord('a')]
        return res
