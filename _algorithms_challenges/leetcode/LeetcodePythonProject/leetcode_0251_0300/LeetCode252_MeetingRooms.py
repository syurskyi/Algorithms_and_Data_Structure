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
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x.start)
        length = len(intervals)
        for i in range(length-1):
            curr = intervals[i]
            nextInter = intervals[i+1]
            if curr.end > nextInter.start:
                return False
        return True
