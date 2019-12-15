'''
Created on Mar 8, 2017

@author: MT
'''

import heapq
class MedianFinder(object):
    def __init__(self):
        # minHeap save positive values: 7, 9
        self.minHeap = []
        # maxHeap save negative values: -5, -3, -2
        self.maxHeap = []

    def addNum(self, num):
        if (not self.minHeap and not self.maxHeap) or num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
            if len(self.maxHeap) > len(self.minHeap) + 1:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        else:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) > len(self.maxHeap):
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
    
    def findMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0])/2.0
        else:
            return -self.maxHeap[0]
