'''
Created on Sep 19, 2017

@author: MT
'''
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        import heapq
        pq = [(arr[0], i, 0) for i, arr in enumerate(nums)]
        heapq.heapify(pq)
        res = [float('-inf'), float('inf')]
        right = max([arr[0] for arr in nums])
        while pq:
            left, i, j = heapq.heappop(pq)
            if right-left < res[1]-res[0]:
                res = [left, right]
            if j+1 == len(nums[i]):
                return res
            v = nums[i][j+1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j+1))
        return res
    
    def test(self):
        testCases = [
            [
                [4, 10, 15, 24, 26],
                [0, 9, 12, 20],
                [5, 18, 22, 30],
            ],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.smallestRange(nums)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
