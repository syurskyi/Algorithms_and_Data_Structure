'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end = 1, x
        while start <= end:
            mid = (start+end)/2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                start = mid+1
            else:
                end = mid-1
        return start if start == 0 else start-1
    
    def test(self):
        pass

if __name__ == '__main__':
    Solution().test()