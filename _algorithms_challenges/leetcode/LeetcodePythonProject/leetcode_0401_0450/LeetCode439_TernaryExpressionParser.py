'''
Created on Apr 17, 2017

@author: MT
'''

class Solution(object):
    def parseTernary(self, expression):
        if not expression: return ''
        stack = []
        for i in range(len(expression)-1, -1, -1):
            c = expression[i]
            if stack and stack[-1] == '?':
                stack.pop()
                first = stack.pop()
                stack.pop()
                second = stack.pop()
                if c == 'T':
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(c)
        return stack[-1]
    
    def parseTernary_own(self, expression):
        if len(expression) == 1:
            return expression
        if expression[0] == 'T':
            subExp = ''
            i = 2
            count = 0
            while i < len(expression):
                if expression[i] == '?':
                    count += 1
                elif expression[i] == ':':
                    count -= 1
                    if count == -1:
                        subExp = expression[2:i]
                        break
                i+=1
        else:
            subExp = ''
            i = 2
            count = 0
            while i < len(expression):
                if expression[i] == '?':
                    count += 1
                elif expression[i] == ':':
                    count -= 1
                    if count == -1:
                        subExp = expression[i+1:]
                        break
                i+=1
        if len(subExp) == 1:
            return subExp
        else:
            return self.parseTernary(subExp)
