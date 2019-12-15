'''
Created on Apr 4, 2017

@author: MT
'''

class Solution(object):
    def deconString(self, s):
        stack = [['', 1]]
        num = ''
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append(['', int(num)])
                num = ''
            elif c == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += c
        return stack[0][0]
    
    def decodeString_own(self, s):
        if '[' not in s:
            return s
        result = ''
        i, n = 0, len(s)
        while i < n:
            c = s[i]
            if c == '[':
                count = 1
                j = i+1
                while j < len(s) and count > 0:
                    if s[j] == '[':
                        count+=1
                    elif s[j] == ']':
                        count-=1
                    j+=1
                nextInd = j
                subStr = s[i+1:j-1]
                tmp = self.decodeString(subStr)
                j = i
                while j-1 >= 0 and s[j-1].isdigit():
                    j-=1
                times = int(s[j:i])
                result += times*tmp
                i = nextInd
            elif not c.isdigit():
                result += c
                i += 1
            else:
                i += 1
        return result
