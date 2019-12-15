'''
Created on Jan 11, 2017

@author: MT
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0: return []
        res = []
        self.dfs(n, n, '', res)
        return res
    
    def dfs(self, left, right, curr, res):
        if left == 0 and right == 0:
            res.append(curr)
        if left > right:
            return
        if left > 0:
            self.dfs(left-1, right, curr+'(', res)
        if right > 0:
            self.dfs(left, right-1, curr+')', res)
    
    def test(self):
        for n in range(4):
            print('n: %s' % n)
            result = self.generateParenthesis(n)
            print('result: %s' % result)
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()
