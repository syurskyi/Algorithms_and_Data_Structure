'''
Created on Apr 17, 2018

@author: tongq
'''
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        arr, l, r = A, L, R
        res = 0
        j = 0
        count = 0
        for i in range(len(arr)):
            if l <= arr[i] <= r:
                res += i-j+1
                count = i-j+1
            elif arr[i] < l:
                res += count
            else:
                j = i+1
                count = 0
        return res
    
    def test(self):
        testCases = [
            [
                [2, 1, 4, 3],
                2, 3,
            ],
            [
                [73,55,36,5,55,14,9,7,72,52],
                32, 69,
            ],
            [
                [2,9,2,5,6],
                2, 8
            ],
        ]
        for arr, l, r in testCases:
            result = self.numSubarrayBoundedMax(arr, l, r)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
