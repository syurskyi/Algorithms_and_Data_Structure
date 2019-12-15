'''
Created on Oct 29, 2019

@author: tongq
'''
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = sum(A)
        sumB = sum(B)
        evenNum = (sumA+sumB)//2
        setA = set(A)
        setB = set(B)
        ans = [0, 0]
        for a in setA:
            if evenNum - (sumA - a) in setB:
                ans[0] = a
                ans[1] = evenNum - (sumA-a)
                return ans
