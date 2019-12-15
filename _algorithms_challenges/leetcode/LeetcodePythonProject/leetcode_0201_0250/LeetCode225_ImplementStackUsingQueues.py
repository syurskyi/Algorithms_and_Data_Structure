'''
Created on Feb 22, 2017

@author: MT
'''

class Solution(object):
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    
    def push(self, x):
        if self.empty():
            self.queue1.append(x)
        else:
            if self.queue1:
                self.queue2.append(x)
                while self.queue1:
                    self.queue2.append(self.queue1.pop(0))
            else:
                self.queue1.append(x)
                while self.queue2:
                    self.queue1.append(self.queue2.pop(0))
    
    def pop(self):
        if self.queue1:
            return self.queue1.pop(0)
        else:
            return self.queue2.pop(0)
    
    def top(self):
        if self.queue1:
            return self.queue1[0]
        else:
            return self.queue2[0]
    
    def empty(self):
        return not self.queue1 and not self.queue2

if __name__ == '__main__':
    stack = Solution()
    stack.push(123)
    stack.push('a')
    print(stack.top())
    print(stack.pop())
    print(stack.top())
