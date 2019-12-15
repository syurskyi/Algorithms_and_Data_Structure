'''
Created on Apr 5, 2018

@author: tongq
'''
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j, s = J, S
        jset = set(list(j))
        res = 0
        for c in s:
            if c in jset:
                res += 1
        return res
    
    def test(self):
        testCases = [
            [
                'aA',
                'aAAbbbb',
            ],
            [
                'z',
                'ZZ',
            ],
        ]
        for j, s in testCases:
            print('j: %s' % j)
            print('s: %s' % s)
            result = self.numJewelsInStones(j, s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
