'''
Created on Apr 17, 2017

@author: MT
'''

class Solution(object):
    def arrangeCoins(self, n):
        start, end = 1, n
        while start <= end:
            mid = (start+end)/2
            if mid*(mid+1)/2 > n:
                end = mid-1
            else:
                start = mid+1
        return start-1
