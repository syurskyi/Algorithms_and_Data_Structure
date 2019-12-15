'''
Created on Sep 25, 2017

@author: MT
'''
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        res = [0]*n
        prevTime = 0
        for log in logs:
            arr = log.split(':')
            if stack:
                res[stack[-1]] += int(arr[2])-prevTime
            prevTime = int(arr[2])
            if arr[1] == 'start':
                stack.append(int(arr[0]))
            else:
                res[stack.pop()] += 1
                prevTime += 1
        return res
    
    def test(self):
        testCases = [
            [
                2,
                [
                    "0:start:0",
                    "1:start:2",
                    "1:end:5",
                    "0:end:6",
                ],
            ],
        ]
        for n, logs in testCases:
            print('n: %s' % n)
            print('logs: %s' % logs)
            result = self.exclusiveTime(n, logs)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
