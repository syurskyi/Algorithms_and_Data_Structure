'''
Created on Apr 5, 2017

@author: MT
'''

class Solution(object):
    def findNthDigit(self, n):
        length, count, start = 1, 9, 1
        while n > length*count:
            n -= length*count
            length += 1
            count *= 10
            start *= 10
        start += (n-1)//length
        s = str(start)
        return int(s[(n-1)%length])
    
    def test(self):
        testCases = [
            3,
            11,
            250,
            300,
        ]
        for num in testCases:
            print('num: %s' % num)
            result = self.findNthDigit(num)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
