'''
Created on Feb 20, 2017

@author: MT
'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        elem = []
        result = []
        self.helper(elem, 1, k, n, result)
        return result
    
    def helper(self, elem, start, k, n, result):
        if len(elem) == k and n == 0:
            result.append(list(elem))
            return
        if n < 0:
            return
        for i in range(start, 10):
            elem.append(i)
            self.helper(elem, i+1, k, n-i, result)
            elem.pop()
    
    def test(self):
        testCases = [
            (3, 7),
            (3, 9),
        ]
        for k, n in testCases:
            print('k: %s' % (k))
            print('n: %s' % (n))
            result = self.combinationSum3(k, n)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
