'''
Created on Feb 13, 2017

@author: MT
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
            mod = (n-1)%26
            res = chr(mod+ord('A'))+res
            n = int((n-mod)/26)
        return res
    
    def test(self):
        for n in range(30):
            print('n: %s' % (n))
            result = self.convertToTitle(n)
            print('result: %s' % (result))
            print('-='*20 + '-')

if __name__ == '__main__':
    Solution().test()