'''
Created on Mar 11, 2017

@author: MT
'''

class Solution(object):
    def removeInvalidParentheses(self, s):
        rmL, rmR = 0, 0
        for c in s:
            if c == '(':
                rmL += 1
            elif c == ')':
                if rmL > 0:
                    rmL -= 1
                else:
                    rmR += 1
        result = set()
        self.helper(s, 0, result, '', rmL, rmR, 0)
        return list(result)
    
    def helper(self, s, i, result, elem, rmL, rmR, openNum):
        if rmL < 0 or rmR < 0 or openNum < 0:
            return
        if i == len(s):
            if rmL == 0 and rmR == 0 and openNum == 0:
                result.add(elem)
            return
        c = s[i]
        if c == '(':
            self.helper(s, i+1, result, elem+c, rmL, rmR, openNum+1)
            self.helper(s, i+1, result, elem, rmL-1, rmR, openNum)
        elif c == ')':
            self.helper(s, i+1, result, elem+c, rmL, rmR, openNum-1)
            self.helper(s, i+1, result, elem, rmL, rmR-1, openNum)
        else:
            self.helper(s, i+1, result, elem+c, rmL, rmR, openNum)
    
    def test(self):
        testCases = [
            '()())()',
            '(a)())()',
            ')(',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.removeInvalidParentheses(s)
            print('result: %s' % (result))
            print('-='*20+'-')
    
if __name__ == '__main__':
    Solution().test()
