'''
Created on Apr 19, 2018

@author: tongq
'''
class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        r, g, b = color[1:3].lower(), color[3:5].lower(), color[5:7].lower()
        print(r, g, b)
        return '#' + self.getTwoDigits(r) + self.getTwoDigits(g) + self.getTwoDigits(b)
    
    def getTwoDigits(self, s):
        res = 0
        diff = float('inf')
        for s0 in ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99',\
                   'aa', 'bb', 'cc', 'dd', 'ee', 'ff']:
            num0 = self.convert(s0)
            num = self.convert(s)
            diff0 = (num0-num)**2
            if diff0 < diff:
                res = s0
                diff = diff0
        return res
    
    def convert(self, s):
        num = 16*(ord(s[0])-ord('0') if s[0].isdigit() else ord(s[0])-ord('a')+10)
        num += (ord(s[1])-ord('0') if s[1].isdigit() else ord(s[1])-ord('a')+10)
        return num
    
    def test(self):
        testCases = [
            '#09f166',
        ]
        for color in testCases:
            print('color: %s' % color)
            result = self.similarRGB(color)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
