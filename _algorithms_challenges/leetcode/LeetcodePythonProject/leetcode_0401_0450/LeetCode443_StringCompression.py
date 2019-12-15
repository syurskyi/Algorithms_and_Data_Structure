'''
Created on Nov 15, 2017

@author: MT
'''
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        res = 0
        i = 0
        j = 0
        n = len(chars)
        while i < n:
            if i+1 < n and chars[i+1] == chars[i]:
                chars[j] = chars[i]
                j += 1
                prev = i
                while i+1 < n and chars[i+1] == chars[i]:
                    i += 1
                numStr = str(i-prev+1)
                for c0 in numStr:
                    chars[j] = c0
                    j += 1
                res += 1+len(numStr)
            else:
                chars[j] = chars[i]
                j += 1
                res += 1
            i += 1
        return res
    
    def test(self):
        testCases = [
            'aabbccc',
            'a',
            'abbbbbbbbbbbbb'
        ]
        for chars in testCases:
            chars = list(chars)
            print('chars: %s' % chars)
            result = self.compress(chars)
            print('result: %s' % result)
            print('chars: %s' % chars)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
