'''
Created on Mar 1, 2017

@author: MT
'''
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        import heapq
        intervals.sort(key=lambda x: x.start)
        heap = []
        maxLen = 0
        for interval in intervals:
            while heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
            maxLen = max(maxLen, len(heap))
        return maxLen
     
    def test(self):
        testCases = [
            [[0, 30], [5, 10], [15, 20]],
            [[0, 50], [5, 10], [15, 20], [17, 23], [19, 30]],
            [[13, 15], [0, 13]],
            [[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]],
        ]
        for intervals in testCases:
            print('intervals: %s' % (intervals))
            intervals = [Interval(inter[0], inter[1]) for inter in intervals]
            result = self.minMeetingRooms(intervals)
            print('result: %s' % result)
            print('-='*20+'-')

def main():
    Solution().test()

if __name__ == '__main__':
    main()

