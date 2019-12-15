'''
Created on Aug 20, 2017

@author: MT
'''

class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        l = list(range(1, n+1))
        return self.helper(l)
    
    def helper(self, l):
        if len(l) <= 2:
            return '(%s,%s)' % (l[0], l[1])
        l0 = []
        while l:
            l0.append('(%s,%s)' % (l.pop(0), l.pop()))
        res = self.helper(l0)
        return res
    
    def test(self):
        testCases = [
            2,
            4,
            8,
        ]
        for n in testCases:
            print('n: %s' % n)
            res = self.findContestMatch(n)
            print('result: %s' % res)
            print('-='*30+'-')
    
if __name__ == '__main__':
    Solution().test()
