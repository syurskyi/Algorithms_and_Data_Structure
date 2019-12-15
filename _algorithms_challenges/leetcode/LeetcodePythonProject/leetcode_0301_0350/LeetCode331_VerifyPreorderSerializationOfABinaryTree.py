'''
Created on Mar 19, 2017

@author: MT
'''

class Solution(object):
    def isValidSerialization(self, preorder):
        if not preorder: return False
        nodes = preorder.split(',')
        stack = []
        for node in nodes:
            stack.append(node)
            while len(stack)>=3 and stack[-1] == '#' and stack[-2] == '#' and\
                stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
        return stack == ['#']
