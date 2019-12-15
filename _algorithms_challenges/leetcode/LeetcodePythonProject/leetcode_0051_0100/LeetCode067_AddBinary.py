'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a and not b: return ''
        if not a: return b
        if not b: return a
        if len(a) < len(b):
            tmp = a
            a = b
            b = tmp
        length1 = len(a)
        length2 = len(b)
        result = ''
        i1, i2 = length1-1, length2-1
        carry = False
        while i2 >= 0:
            c1 = a[i1]
            c2 = b[i2]
            if c1 == '0' and c2 == '0':
                if carry:
                    result = '1' + result
                else:
                    result = '0' + result
                carry = False
            elif c1 == '1' and c2 == '1':
                if carry:
                    result = '1' + result
                else:
                    result = '0' + result
                carry = True
            else:
                if carry:
                    result = '0' + result
                    carry = True
                else:
                    result = '1' + result
                    carry = False
            i1 -= 1
            i2 -= 1
        if carry:
            if i1 == -1:
                result = '1' + result
            else:
                tmp = self.addBinary(a[:i1+1], '1')
                result = tmp + result
        else:
            result = a[:i1+1]+ result
        return result
    
    def test(self):
        testCases = [
            ('11', '1'),
            ('1', '1'),
            ('1', '110'),
        ]
        for a, b in testCases:
            print('a: %s, b: %s' % (a, b))
            result = self.addBinary(a, b)
            print('result: %s' % result)
            print('-='*15 + '-')

if __name__ == '__main__':
    Solution().test()