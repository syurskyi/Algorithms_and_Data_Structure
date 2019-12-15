'''
Created on Sep 5, 2017

@author: MT
'''

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        minA, minB = float('inf'), float('inf')
        for a, b in ops:
            minA = min(minA, a)
            minB = min(minB, b)
        return min(minA, m)*min(minB, n)
    
    def test(self):
        testCases = [
            
        ]
        

if __name__ == '__main__':
    Solution().test()
