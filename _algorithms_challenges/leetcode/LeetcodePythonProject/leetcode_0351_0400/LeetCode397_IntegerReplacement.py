'''
Created on Apr 5, 2017

@author: MT
'''

class Solution(object):
    def integerReplacement(self, n):
        steps = 0
        while n > 1:
            steps += 1
            if n%2 == 0:
                n /= 2
            else:
                if (n+1)%4 == 0 and n != 3:
                    n += 1
                else:
                    n -= 1
        return steps
