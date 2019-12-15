'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object):
    def __init__(self, nums):
        self.nums = nums
    
    def reset(self):
        return self.nums
    
    def shuffle(self):
        import random
        newNums = list(self.nums)
        if not newNums:
            return newNums
        for i in range(len(newNums)-1, 0, -1):
            ind = random.randint(0, i)
            newNums[ind], newNums[i] = newNums[i], newNums[ind]
        return newNums
