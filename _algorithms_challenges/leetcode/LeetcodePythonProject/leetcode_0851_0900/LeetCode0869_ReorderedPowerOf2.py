'''
Created on Sep 30, 2019

@author: tongq
'''
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        n = N
        if n == 1: return True
        s = str(n)
        length = len(s)
        nums = self.getNums(length)
        for num in nums:
            if self.matches(n, num):
                return True
        return False
    
    def matches(self, n, num):
        hashmap = {}
        for c in str(n):
            if c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1
        for c in str(num):
            if c in hashmap:
                hashmap[c] -= 1
                if hashmap[c] == 0:
                    del hashmap[c]
            else:
                return False
        return True
    
    def getNums(self, length):
        res = []
        num = 2
        while len(str(num)) < length:
            num *= 2
        while len(str(num)) == length:
            res.append(num)
            num *= 2
        return res
