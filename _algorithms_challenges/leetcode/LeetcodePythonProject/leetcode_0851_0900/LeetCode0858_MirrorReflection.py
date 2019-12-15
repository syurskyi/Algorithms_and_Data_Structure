'''
Created on Sep 16, 2019

@author: tongq
'''
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        while p % 2 == 0 and q % 2 == 0:
            p, q = p//2, q//2
        if p % 2 == 0:
            return 2
        elif q % 2 == 0:
            return 0
        else:
            return 1
    
    def test(self):
        testCases = [
            
        ]
        for p, q in testCases:
            res = self.mirrorReflection(p, q)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
