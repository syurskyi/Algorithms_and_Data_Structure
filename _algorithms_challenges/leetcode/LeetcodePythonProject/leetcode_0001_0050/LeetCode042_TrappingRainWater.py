'''
Created on Jun 5, 2018

@author: tongq
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        n = len(height)
        left = [0]*n
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(height[i], left[i-1])
        right = [0]*n
        right[-1] = height[-1]
        for i in range(n-2, -1, -1):
            right[i] = max(height[i], right[i+1])
        res = 0
        for i in range(n):
            res += min(left[i], right[i])-height[i]
        return res
