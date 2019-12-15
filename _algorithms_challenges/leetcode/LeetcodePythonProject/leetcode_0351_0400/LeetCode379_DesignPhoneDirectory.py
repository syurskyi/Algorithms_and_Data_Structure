'''
Created on Apr 1, 2017

@author: MT
'''

class PhoneDirectory(object):
    def __init__(self, maxNumbers):
        self.availableNums = set(range(maxNumbers))
        self.usedNums = set()
    
    def get(self):
        if self.availableNums:
            num = self.availableNums.pop()
            self.usedNums.add(num)
            return num
        else:
            return -1
    
    def check(self, number):
        return bool(number in self.availableNums)
    
    def release(self, number):
        if number in self.usedNums:
            self.usedNums.remove(number)
        self.availableNums.add(number)
    
