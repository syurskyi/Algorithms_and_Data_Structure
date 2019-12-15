'''
Created on Jan 24, 2017

@author: MT
'''

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n <= 0 or n < k:
            return []
        result = []
        elem = []
        self.helper(elem, result, 1, n, k)
        return result
    
    def helper(self, elem, result, start, n, k):
        if len(elem) == k:
            result.append(list(elem))
            return
        for i in range(start, n+1):
            elem.append(i)
            self.helper(elem, result, i+1, n, k)
            del elem[-1]
    
    def test(self):
        testCases = [
            (4, 2),
        ]
        for n, k in testCases:
            print('n: %s, k: %s' % (n, k))
            result = self.combine(n, k)
            print('result: %s' % (result))
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()
