'''
Created on Mar 29, 2017

@author: MT
'''

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        import heapq
        heap = []
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(heap, (num1+num2, num1, num2))
        result = []
        for _ in range(k):
            if not heap:
                break
            _, num1, num2 = heapq.heappop(heap)
            result.append((num1, num2))
        return result
    
    def test(self):
        testCases = [
            (
                [1, 7, 11],
                [2, 4, 6],
                3
            ),
            (
                [1, 1, 2],
                [1, 2, 3],
                2,
            ),
            (
                [1, 2],
                [3],
                3,
            ),
        ]
        for nums1, nums2, k in testCases:
            print('nums1: %s' % nums1)
            print('nums2: %s' % nums2)
            print('k: %s' % k)
            result = self.kSmallestPairs(nums1, nums2, k)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
