'''
Created on Apr 27, 2017

@author: MT
'''
import heapq

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        pass
    
    
    def medianSlidingWindow_another(self, nums, k):
        import bisect
        window = sorted(nums[:k])
        medians = []
        for a, b in zip(nums, nums[k:]+[0]):
            medians.append((window[k/2] + window[~(k/2)]/2.0))
            window.remove(a)
            bisect.insort(window, b)
        return medians
    
    
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
    
    def getMedian(self):
        if not self.maxHeap and not self.minHeap:
            return 0
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0])/2.0
        else:
            return float(self.minHeap[0])
    
    def add(self, num):
        if not self.maxHeap or num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        if len(self.maxHeap) > len(self.minHeap):
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        if len(self.minHeap) > len(self.maxHeap)+1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
    
    def remove(self, num):
        if num >= self.getMedian():
            self.minHeap.remove(num)
            heapq.heapify(self.minHeap)
        else:
            self.maxHeap.remove(-num)
            heapq.heapify(self.maxHeap)
        if len(self.maxHeap) > len(self.minHeap):
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        if len(self.minHeap) > len(self.maxHeap)+1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
    
    def medianSlidingWindow_slow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        n = len(nums) - k + 1
        result = [0.0]*n
        for i in range(len(nums)+1):
            if i >= k:
                result[i-k] = self.getMedian()
                self.remove(nums[i-k])
            if i < len(nums):
                self.add(nums[i])
        return result
