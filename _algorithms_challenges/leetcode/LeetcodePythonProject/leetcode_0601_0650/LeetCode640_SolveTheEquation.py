'''
Created on Sep 27, 2017

@author: MT
'''
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        arr = equation.split('=')
        s1 = arr[0]
        s2 = arr[1]
        valX1, val1 = self.solveHelper(s1)
        valX2, val2 = self.solveHelper(s2)
#         print('valX1, val1: %s, %s' % (valX1, val1))
#         print('valX2, val2: %s, %s' % (valX2, val2))
        if val1 == val2:
            if valX1 == valX2:
                return 'Infinite solutions'
            else:
                return 'x=0'
        else:
            if valX1 == valX2:
                return 'No solution'
            else:
                val = (val2-val1)//(valX1-valX2)
                return 'x=%s' % val
    
    def solveHelper(self, s):
        valX1, val1 = 0, 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                sig = 1
                if i>=1 and s[i-1] == '-':
                    sig = -1
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = 10*num+int(s[i])
                    i += 1
                if i < len(s) and s[i] == 'x':
                    valX1 += num*sig
                    i += 1
                else:
                    val1 += num*sig
            elif s[i] == 'x':
                if i == 0:
                    valX1 += 1
                elif s[i-1] == '-':
                    valX1 -= 1
                elif s[i-1] == '+':
                    valX1 += 1
            i += 1
        return valX1, val1
    
    def test(self):
        testCases = [
            'x+5-3+x=6+x-2',
            'x=x',
            '2x=x',
            '2x+3x-6x=x+2',
            'x=x+2',
        ]
        for equation in testCases:
            print('equation: %s' % equation)
            result = self.solveEquation(equation)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
