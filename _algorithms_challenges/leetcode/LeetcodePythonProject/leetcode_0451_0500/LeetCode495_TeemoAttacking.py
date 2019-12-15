'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    def findPoisonedDurationAnother(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries: return 0
        res = 0
        for i in range(1, len(timeSeries)):
            res += min(timeSeries[i]-timeSeries[i-1], duration)
        res += duration
        return res
    
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        result = 0
        prev = 0
        maxTime = 0
        for time in timeSeries:
            if maxTime < time:
                result += maxTime - prev
                prev = time
            maxTime = max(maxTime, time+duration)
        result += maxTime-prev
        return result
    
    def test(self):
        testCases = [
            [
                [1, 4],
                2,
            ],
            [
                [1, 2],
                2,
            ],
        ]
        for timeSeries, duration in testCases:
            print('timeSeries: %s' % timeSeries)
            print('duration: %s' % duration)
            result = self.findPoisonedDurationAnother(timeSeries, duration)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
