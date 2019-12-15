'''
Created on Mar 11, 2017

@author: MT
'''

class NumArray(object):
    def __init__(self, nums):
        self.dp = [0]
        for num in nums:
            self.dp.append(self.dp[-1] + num)
    
    def sumRange(self, i, j):
        return self.dp[j+1] - self.dp[i]
