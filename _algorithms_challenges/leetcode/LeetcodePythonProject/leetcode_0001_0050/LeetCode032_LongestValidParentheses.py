'''
Created on Mar 14, 2017

@author: MT
'''

class Solution(object):
    def longestValidParentheses(self, s):
        left = -1
        stack = []
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        res = max(res, i-stack[-1])
                    else:
                        res = max(res, i-left)
                else:
                    left = i
        return res
    
    def test(self):
        testCases = [
            '()',
            '(()',
            ')()())',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.longestValidParentheses(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
