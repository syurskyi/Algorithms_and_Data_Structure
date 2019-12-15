'''
Created on Oct 21, 2017

@author: MT
'''
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        valids = []
        res = 0
        for c in ops:
            if c == '+':
                res += valids[-1]+valids[-2]
                valids.append(valids[-1]+valids[-2])
            elif c == 'D':
                res += valids[-1]*2
                valids.append(valids[-1]*2)
            elif c == 'C':
                d = valids.pop()
                res -= d
            else:
                res += int(c)
                valids.append(int(c))
        return res
    
    def test(self):
        testCases = [
#             ["5","2","C","D","+"],
            ["5","-2","4","C","D","9","+","+"],
        ]
        for ops in testCases:
            print('ops: %s' % ops)
            result = self.calPoints(ops)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
