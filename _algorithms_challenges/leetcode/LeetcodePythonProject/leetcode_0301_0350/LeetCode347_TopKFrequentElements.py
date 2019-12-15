'''
Created on Mar 21, 2017

@author: MT
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        maxCount = 0
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0)+1
            maxCount = max(maxCount, hashmap[num])
        dp = [[] for _ in range(maxCount)]
        for num, count in hashmap.items():
            dp[count-1].append(num)
        result = []
        i = maxCount-1
        while k > 0:
            if i < 0:
                break
            if not dp[i]:
                i-=1
            else:
                result.append(dp[i].pop(0))
                k-=1
        return result
        
    
    def topKFrequentHeap(self, nums, k):
        import heapq
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0)+1
        heap = []
        for num, count in hashmap.items():
            heapq.heappush(heap, (-count, num))
        result = []
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        return result
    
    def test(self):
        testCases = [
#             ([1, 1, 1, 2, 2, 3], 2),
            ([1,1,1,2,2,2,3,3,3], 3),
        ]
        for nums, k in testCases:
            print('nums: %s' % (nums))
            print('k: %s' % (k))
            result = self.topKFrequent(nums, k)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
