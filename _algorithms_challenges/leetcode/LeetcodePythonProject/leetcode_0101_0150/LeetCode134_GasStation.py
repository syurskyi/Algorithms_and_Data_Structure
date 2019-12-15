'''
Created on Feb 8, 2017

@author: MT
'''

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sumRemaining, sumVal, start = 0, 0, 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            remain = g-c
            if sumRemaining >= 0:
                sumRemaining += remain
            else:
                sumRemaining = remain
                start = i
            sumVal += remain
        if sumVal >= 0:
            return start
        else:
            return -1
    