'''
Created on Feb 23, 2017

@author: MT
'''
class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, x):
        if self.empty():
            self.stack1.append(x)
        elif self.stack1:
            self.stack1.append(x)
        else:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            self.stack1.append(x)
    
    def pop(self):
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
    def peep(self):
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    
    def empty(self):
        return not self.stack1 and not self.stack2
