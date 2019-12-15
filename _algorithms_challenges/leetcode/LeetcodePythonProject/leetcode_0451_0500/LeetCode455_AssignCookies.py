'''
Created on Apr 20, 2017

@author: MT
'''

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j = 0, 0
        count = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
                count += 1
            else:
                j += 1
        return count
    
    def test(self):
        testCases = [
            ([1,2,3], [1,1]),
            ([1,2], [1,2,3]),
            ([10,9,8,7], [5,6,7,8]),
        ]
        for g, s in testCases:
            print('g: %s' % g)
            print('s: %s' % s)
            result = self.findContentChildren(g, s)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

