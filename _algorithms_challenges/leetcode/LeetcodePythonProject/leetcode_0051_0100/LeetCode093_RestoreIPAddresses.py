'''
Created on May 30, 2018

@author: tongq
'''
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12: return []
        res = []
        self.helper(res, [], s, 0)
        return res
    
    def helper(self, res, curr, s, ind):
        if ind == len(s) and len(curr) == 4:
            res.append('.'.join(curr))
        if ind >= len(s):
            return
        for i in range(ind+1, ind+4):
            sub = s[ind:i]
            if sub[0] == '0' and len(sub) > 1:
                break
            if int(sub) > 255:
                break
            curr.append(sub)
            self.helper(res, curr, s, i)
            curr.pop()
