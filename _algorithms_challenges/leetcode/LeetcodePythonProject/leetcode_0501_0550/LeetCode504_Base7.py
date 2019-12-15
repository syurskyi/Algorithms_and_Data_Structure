'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num = -num
            sig = '-'
        else:
            sig = ''
        res = ''
        while num > 0:
            digit = num%7
            res = str(digit)+res
            num = int((num-digit)/7)
        if not res:
            return '0'
        else:
            return sig+res
    
    def test(self):
        testCases = [
            100,
            -7,
        ]
        for num in testCases:
            result = self.convertToBase7(num)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
