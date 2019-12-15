'''
Created on Feb 12, 2017

@author: MT
'''

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return False
        m, n = len(t), len(s)
        if abs(m-n) > 1:
            return False
        i, j, count = 0, 0, 0
        while i < n and j < m:
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                count+=1
                if count>1:
                    return False
                if m>n:
                    j+=1
                elif n>m:
                    i+=1
                else:
                    i+=1
                    j+=1
        if i < n or j < m:
            count += 1
        if count == 1:
            return True
        return False
    
    def test(self):
        pass

if __name__ == '__main__':
    Solution().test()
