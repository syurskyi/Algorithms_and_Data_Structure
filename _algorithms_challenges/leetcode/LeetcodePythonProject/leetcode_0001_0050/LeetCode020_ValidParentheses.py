'''
Created on Nov 6, 2017

@author: MT
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if  (c == ')' and stack and stack[-1]=='(') or\
                    (c == ']' and stack and stack[-1]=='[') or\
                    (c == '}' and stack and stack[-1]=='{'):
                    stack.pop()
                else:
                    return False
        return stack == []
    
    def test(self):
        testCases = [
            '(){}[]',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.isValid(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
