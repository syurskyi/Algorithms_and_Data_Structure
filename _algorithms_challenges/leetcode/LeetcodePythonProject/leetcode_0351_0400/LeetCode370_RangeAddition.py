'''
Created on Mar 29, 2017

@author: MT
'''

class Solution(object):
    def getModifiedArray(self, length, updates):
        result = [0]*length
        for update in updates:
            start = update[0]
            end = update[1]
            increase = update[2]
            result[start] += increase
            if end < length-1:
                result[end+1] -= increase
        val = 0
        for i in range(length):
            val += result[i]
            result[i] = val
        return result
