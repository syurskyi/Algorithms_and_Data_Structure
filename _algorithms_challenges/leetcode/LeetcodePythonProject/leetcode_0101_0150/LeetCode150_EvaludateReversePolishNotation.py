'''
Created on Feb 11, 2017

@author: MT
'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import operator
        stack = []
        for token in tokens:
            if token == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1+num2)
            elif token == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2-num1)
            elif token == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)
            elif token == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(operator.truediv(num2, num1) ))
            else:
                stack.append(int(token))
        return stack[-1]
    
    def test(self):
        testCases = [
#             ["2", "1", "+", "3", "*"],
#             ["4", "13", "5", "/", "+"],
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
        ]
        for tokens in testCases:
            print('tokens: %s' % (tokens))
            result = self.evalRPN(tokens)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()