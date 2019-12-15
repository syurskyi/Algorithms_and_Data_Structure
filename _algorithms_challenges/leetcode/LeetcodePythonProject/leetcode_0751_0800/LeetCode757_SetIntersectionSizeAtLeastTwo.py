'''
Created on Mar 30, 2018

@author: tongq
'''
class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        for interval in intervals:
            while stack and stack[-1][1] >= interval[1]:
                stack.pop()
            stack.append(interval)
        n = len(stack)
        a = [[0, 0] for _ in range(n)]
        for i in range(n-1, -1, -1):
            a[i][0] = stack[-1][0]
            a[i][1] = stack.pop()[1]
        res = 2
        p1 = a[0][1]-1
        p2 = a[0][1]
        for i in range(1, n):
            bo1 = p1 >= a[i][0] and p1 <= a[i][1]
            bo2 = p2 >= a[i][0] and p2 <= a[i][1]
            if bo1 and bo2:
                continue
            if bo2:
                p1 = p2
                p2 = a[i][1]
                res += 1
                continue
            p1 = a[i][1]-1
            p2 = a[i][1]
            res += 2
        return res
    
    def test(self):
        testCases = [
            [[1, 3], [1, 4], [2, 5], [3, 5]],
            [[1, 2], [2, 3], [2, 4], [4, 5]],
        ]
        for intervals in testCases:
            print('intervals: %s' % intervals)
            result = self.intersectionSizeTwo(intervals)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
