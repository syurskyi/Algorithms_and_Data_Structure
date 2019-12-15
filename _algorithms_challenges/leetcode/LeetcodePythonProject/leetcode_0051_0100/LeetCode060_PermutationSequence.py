'''
Created on Jan 22, 2017

@author: MT
'''
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = list(range(1, n+1))
        k -= 1
        mod = 1
        for i in range(n):
            mod = mod*(i+1)
        res = ''
        for i in range(n):
            mod = mod//(n-i)
            curInd = k//mod
            k = k % mod
            res += str(nums[curInd])
            nums.pop(curInd)
        return res
