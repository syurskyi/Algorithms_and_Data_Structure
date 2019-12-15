'''
Created on Feb 27, 2017

@author: MT
'''

class Solution(object):
    def diffWaysToCompute(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = []
        for i, c in enumerate(s):
            if c in ('+', '-', '*'):
                res1 = self.diffWaysToCompute(s[:i])
                res2 = self.diffWaysToCompute(s[i+1:])
                for num1 in res1:
                    for num2 in res2:
                        if c == '+':
                            res.append(num1+num2)
                        elif c == '-':
                            res.append(num1-num2)
                        else:
                            res.append(num1*num2)
        if not res:
            res = [int(s)]
        return res
    
    def test(self):
        testCases = [
            '2-1-1',
            '2*3-4*5',
        ]
        for s in testCases:
            print('input: %s' % s)
            result = self.diffWaysToCompute(s)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
