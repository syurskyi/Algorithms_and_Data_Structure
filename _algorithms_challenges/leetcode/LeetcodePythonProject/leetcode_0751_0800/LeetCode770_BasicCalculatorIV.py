'''
Created on Apr 5, 2018

@author: tongq
'''
class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        pass
    
    def test(self):
        testCases = [
            [
                "e + 8 - a + 5",
                ["e"],
                [1],
            ],
            [
                "e - 8 + temperature - pressure",
                ["e", "temperature"],
                [1, 12],
            ],
            [
                "7 - 7",
                [],
                [],
            ],
            [
                "a * b * c + b * a * c * 4",
                [],
                [],
            ],
            [
                "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
                [],
                [],
            ],
        ]
        for expression, evalvars, evalints in testCases:
            result = self.basicCalculatorIV(expression, evalvars, evalints)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
