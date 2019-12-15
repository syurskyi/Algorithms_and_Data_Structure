'''
Created on Apr 10, 2017

@author: MT
'''

class Solution(object):
    def toHex(self, num):
        if num == 0: return '0'
        mp = '0123456789abcdef'
        result = ''
        for _ in range(8):
            c = mp[num&15]
            result = c + result
            num >>= 4
        return result.lstrip('0')
    
    def test(self):
        testCases = [
            26,
            -1,
        ]
        for num in testCases:
            print('num: %s' % num)
            result = self.toHex(num)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
