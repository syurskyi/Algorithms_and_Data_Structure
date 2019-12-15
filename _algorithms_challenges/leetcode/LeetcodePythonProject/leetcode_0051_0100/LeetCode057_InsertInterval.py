'''
Created on Jan 21, 2017

@author: MT
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
    def __str__(self):
        return '<s: %s, e: %s>' % (self.start, self.end)
    
    def __repr__(self):
        return self.__str__()

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        for interval in intervals:
            if interval.end < newInterval.start:
                result.append(interval)
            elif interval.start > newInterval.end:
                result.append(newInterval)
                newInterval = interval
            elif interval.end >= newInterval.start or interval.start <= newInterval.end:
                newInterval = Interval(\
                    min(newInterval.start, interval.start),\
                    max(newInterval.end, interval.end))
        result.append(newInterval)
        return result
    
    def test(self):
        testCases = [
            ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]),
            ([[1,2],[3,5],[6,7],[8,10],[12,16],[15,23]], [4,9]),
            ([[1,2],[2,5],[6,7],[8,10],[12,16],[15,23]], [7,9]),
        ]
        for intervals, newInterval in testCases:
            intervals = [Interval(x[0], x[1]) for x in intervals]
            newInterval = Interval(newInterval[0], newInterval[1])
            print('intervals: %s' % (intervals))
            result = self.insert(intervals, newInterval)
            print('result: %s' % (result))
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()