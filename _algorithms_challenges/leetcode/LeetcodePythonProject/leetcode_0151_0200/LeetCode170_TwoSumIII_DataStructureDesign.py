'''
Created on Feb 13, 2017

@author: MT
'''
class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.elements = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.elements:
            self.elements[number] += 1
        else:
            self.elements[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.elements:
            target = value-num
            if target in self.elements:
                if target == num and self.elements[target]<2:
                    continue
                return True
        return False