class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A: return 0
        A.sort()
        res = A[-1] - A[0]
        for i in range(len(A)-1):
            minVal = min(A[0]+2*K, A[i+1])
            maxVal = max(A[-1], A[i]+2*K)
            res = min(res, maxVal - minVal)
        return res

    def test(self):
        testCases = [
            # [[1], 0],
            # [[0,10], 2],
            [[1,3,6], 3],
        ]
        for a, k in testCases:
            res = self.smallestRangeII(a, k)
            print('res: %s' % res)
            print('-='*30+'-')


if __name__ == '__main__':
    Solution().test()
