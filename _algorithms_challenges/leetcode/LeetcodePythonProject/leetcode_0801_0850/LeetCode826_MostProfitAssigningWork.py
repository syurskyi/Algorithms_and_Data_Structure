'''
Created on May 5, 2018

@author: tongq
'''
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        arr = [[d, p] for d, p in zip(difficulty, profit)]
        arr.sort()
        p0 = 0
        for i in range(len(arr)):
            p0 = max(p0, arr[i][1])
            arr[i][1] = p0
        res = 0
        worker.sort()
        i = 0
        maxProfit = 0
        for w in worker:
            while i < len(arr) and arr[i][0] <= w:
                maxProfit = max(maxProfit, arr[i][1])
                i += 1
            res += maxProfit
        return res
    
    def test(self):
        testCases = [
            [
                [2,4,6,8,10],
                [10,20,30,40,50],
                [4,5,6,7],
            ],
        ]
        for difficulty, profit, worker in testCases:
            result = self.maxProfitAssignment(difficulty, profit, worker)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
