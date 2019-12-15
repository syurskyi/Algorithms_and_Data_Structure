'''
Created on Sep 17, 2019

@author: tongq
'''
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        arr, k = A, K
        n = len(arr)
        arr2 = [0]*(n+1)
        for i in range(n):
            arr2[i+1] = arr2[i] + arr[i]
        d = []
        res = n+1
        for i in range(n+1):
            while d and arr2[i] - arr2[d[0]] >= k:
                res = min(res, i-d.pop(0))
            while d and arr2[i] <= arr2[d[-1]]:
                d.pop()
            d.append(i)
        return res if res <= n else -1
    
    def test(self):
        testCase = [
            [
                [56,-21,56,35,-9],
                61,
            ],
#             [
#                 [84,-37,32,40,95],
#                 167,
#             ],
#             [
#                 [1],
#                 1,
#             ],
#             [
#                 [1,2],
#                 4
#             ],
#             [
#                 [2,-1,2],
#                 3
#             ],
#             [
#                 [77,19,35,10,-14],
#                 19
#             ],
#             [
#                 [-3, 4, 1],
#                 5,
#             ],
        ]
        for a, k in testCase:
            res = self.shortestSubarray(a, k)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
