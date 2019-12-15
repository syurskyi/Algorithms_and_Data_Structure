'''
Created on May 6, 2018

@author: tongq
'''
class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        import re
        s = S
        if re.match('^[a-z|A-Z]{2,}@[a-z|A-Z]{2,}.[a-z|A-Z]{2,}$', s):
            s = s.lower()
            ind = s.find('@')
            name = s[:ind]
            mail = s[ind:]
            return name[0]+'*****'+name[-1]+mail
        else:
            s0 = re.sub('[{|}|(|)|\+|\-|\s]', '', s)
            if len(s0) == 11 and s0[0] == '1' and s[0]!='+':
                s0 = s0[1:]
            if len(s0) == 10:
                return '***-***-%s' % s0[-4:]
            else:
                cnt = len(s0)-10
                return '+'+'*'*cnt+('-***-***-%s' % s0[-4:])
    
    def test(self):
        testCases = [
            'LeetCode@LeetCode.com',
            'AB@qq.com',
            '1(234)567-890',
            '86-(10)12345678',
            "(3906)2 07143 711",
            "+1(19)5 246 5964",
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.maskPII(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
