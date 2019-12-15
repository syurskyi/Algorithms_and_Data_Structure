'''
Created on Mar 27, 2017

@author: MT
'''

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.hashmap:
            self.hashmap[message] = timestamp
            return True
        else:
            if timestamp - self.hashmap[message] >= 10:
                self.hashmap[message] = timestamp
                return True
            else:
                return False
    