'''
Created on Mar 2, 2017

@author: MT
'''

class Solution(object):
    def isUgly_noRec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0: return False
        while num > 1:
            if num%2 == 0:
                num //= 2
            elif num%3 == 0:
                num //= 3
            elif num%5 == 0:
                num //= 5
            else:
                break
        return num == 1
    
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0: return False
        if num == 1: return True
        if num%2 == 0: return self.isUgly(num/2)
        if num%3 == 0: return self.isUgly(num/3)
        if num%5 == 0: return self.isUgly(num/5)
        return False
