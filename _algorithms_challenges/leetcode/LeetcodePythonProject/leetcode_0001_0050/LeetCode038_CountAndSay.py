'''
Created on Jun 6, 2018

@author: tongq
'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for _ in range(n-1):
            tmp = ''
            i = 0
            while i < len(res):
                count = 1
                while i+1 < len(res) and res[i+1] == res[i]:
                    count += 1
                    i += 1
                tmp += '%s%s' % (count, res[i])
                i += 1
            res = tmp
        return res
