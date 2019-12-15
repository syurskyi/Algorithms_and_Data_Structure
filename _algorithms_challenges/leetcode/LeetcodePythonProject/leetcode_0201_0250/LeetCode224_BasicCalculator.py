'''
Created on Feb 22, 2017

@author: MT
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        stack = []
        sign = 1
        preVal = 0
        while i < len(s):
            if s[i].isdigit():
                preVal = 0
                while i < len(s) and s[i].isdigit():
                    preVal = preVal*10 + int(s[i])
                    i += 1
                i -= 1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif s[i] == ')':
                res += sign*preVal
                res = stack.pop()*res + stack.pop()
                preVal = 0
            elif s[i] == '+':
                res += preVal*sign
                sign = 1
            elif s[i] == '-':
                res += preVal*sign
                sign = -1
            i += 1
        res += preVal*sign
        return res
    
    def test(self):
        testCases = [
            '(1+(4+5+2)-3)+(6+8)',
            '(1-3)+(3-5+(3-10)-10)',
            '3+3-1+(3-3)',
            '4312',
            '1+1',
            '2-1 + 2',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.calculate(s)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
