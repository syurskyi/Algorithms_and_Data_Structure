'''
Created on Oct 7, 2017

@author: MT
'''
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        import bisect, heapq
        ind = bisect.bisect_left(arr, x)
        if ind == 0:
            return arr[:k]
        if ind == len(arr):
            return arr[-k:]
        heap = []
        for i in range(max(0, ind-k), min(len(arr), ind+k)):
            diff = abs(x-arr[i])
            heapq.heappush(heap, (diff, arr[i]))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return sorted(res)
    
    def test(self):
        testCases = [
            [
                [1, 2, 3, 4, 5],
                4,
                3,
            ],
            [
                [1, 2, 3, 4, 5],
                4,
                -1,
            ],
                     [
                [1, 2, 3, 4, 5],
                4,
                9,
            ],
        ]
        for arr, k, x in testCases:
            print('arr: %s' % arr)
            print('k: %s' % k)
            print('x: %s' % x)
            result = self.findClosestElements(arr, k, x)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
