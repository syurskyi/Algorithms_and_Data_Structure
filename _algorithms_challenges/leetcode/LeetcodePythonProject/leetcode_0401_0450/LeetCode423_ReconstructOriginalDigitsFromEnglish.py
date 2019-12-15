'''
Created on Apr 13, 2017

@author: MT
'''

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0]*10
        for c in s:
            if c == 'z': count[0]+=1
            if c == 'w': count[2]+=1
            if c == 'x': count[6]+=1
            if c == 's': count[7]+=1 # 7-6
            if c == 'g': count[8]+=1
            if c == 'u': count[4]+=1
            if c == 'f': count[5]+=1 # 5-4
            if c == 'h': count[3]+=1 # 3-8
            if c == 'i': count[9]+=1 # 9-8-5-6
            if c == 'o': count[1]+=1 # 1-0-2-4
        count[7] -= count[6]
        count[5] -= count[4]
        count[3] -= count[8]
        count[9] = count[9] - count[8] - count[5] - count[6]
        count[1] = count[1] - count[0] - count[2] - count[4]
        result = ''
        for i in range(10):
            result += str(i)*count[i]
        return result