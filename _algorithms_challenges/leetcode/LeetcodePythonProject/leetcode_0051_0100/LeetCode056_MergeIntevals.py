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
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return intervals
        intervals.sort(key=lambda interval: interval.start)
        result = []
        i = 0
        while i < len(intervals):
            curr = intervals[i]
            nextEnd = curr.end
            j = i+1
            while j < len(intervals):
                if intervals[j].start > nextEnd:
                    break
                else:
                    nextEnd = max(intervals[j].end, nextEnd)
                j += 1
            i = j
            result.append(Interval(curr.start, nextEnd))
        
        return result
    
    def test(self):
        testCases = [
            [[1,3],[2,6],[8,10],[15,18]],
            [[1,4],[2,3]],
        ]
        for intervals in testCases:
            intervals = [Interval(x[0], x[1]) for x in intervals]
            print('intervals: %s' % (intervals))
            result = self.merge(intervals)
            print('result: %s' % (result))
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()
    