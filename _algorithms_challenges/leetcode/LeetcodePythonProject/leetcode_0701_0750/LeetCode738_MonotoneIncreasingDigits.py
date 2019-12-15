'''
Created on Mar 14, 2018

@author: tongq
'''
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = str(N)
        i = 0
        while i < len(s)-1 and s[i] <= s[i+1]:
            i += 1
        if i == len(s)-1:
            return N
        while i > 0 and s[i-1] == s[i]:
            i -= 1
        res = s[:i]
        res += str(int(s[i])-1)
        res += '9'*(len(s)-i-1)
        res = res.lstrip('0')
        return int(res) if res != '' else 0
    
    def test(self):
        testCases = [
            10,
            1111,
            1234,
            332,
            1234502468,
            989998,
        ]
        for N in testCases:
            print('N: %s' % N)
            result = self.monotoneIncreasingDigits(N)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
