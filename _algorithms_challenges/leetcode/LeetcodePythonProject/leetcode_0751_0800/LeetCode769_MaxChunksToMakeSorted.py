'''
Created on Apr 4, 2018

@author: tongq
'''
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        maxOfLeft = [0]*n
        minOfRight = [0]*n
        maxOfLeft[0] = arr[0]
        for i in range(1, n):
            maxOfLeft[i] = max(maxOfLeft[i-1], arr[i])
        minOfRight[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            minOfRight[i] = min(minOfRight[i+1], arr[i])
        res = 0
        for i in range(n-1):
            if maxOfLeft[i] <= minOfRight[i+1]:
                res += 1
        return res+1
    
    def test(self):
        testCases = [
            [4,3,2,1,0],
            [1,0,2,3,4],
            [0,2,1,4,3],
        ]
        for arr in testCases:
            print('arr: %s' % arr)
            result = self.maxChunksToSorted(arr)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
