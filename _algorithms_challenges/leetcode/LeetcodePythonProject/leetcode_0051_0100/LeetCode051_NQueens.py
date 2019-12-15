'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n <= 0: return []
        res = []
        self.helper(n, res, [], 0)
        res = self.convert(res)
        return res
    
    def helper(self, n, res, cur, ind):
        if ind == n:
            res.append(list(cur))
            return
        for val in range(n):
            if self.isValid(cur, ind, val):
                cur.append(val)
                self.helper(n, res, cur, ind+1)
                cur.pop()
    
    def convert(self, nums):
        if not nums: return []
        res = []
        for row in nums:
            n = len(row)
            curr = []
            for val in row:
                curr.append('.'*val+'Q'+'.'*(n-val-1))
            res.append(curr)
        return res
    
    def isValid(self, cur, ind, val):
        for i in range(ind):
            if cur[i] == val:
                return False
            if abs(i-ind) == abs(cur[i]-val):
                return False
        return True
    
    def test(self):
        testCases = [
            1,
            2,
            3,
            4,
            5,
        ]
        for n in testCases:
            print('n: %s' % n)
            results = self.solveNQueens(n)
            print('results')
            for res in results:
                print('\n'.join(res))
                print('-'*20)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
