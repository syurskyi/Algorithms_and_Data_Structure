'''
Created on Sep 16, 2019

@author: tongq
'''
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a, b = A, B
        if len(a) != len(b): return False
        if a == b and len(set(a)) < len(a): return True
        dif = [(c1, c2) for c1, c2 in zip(a, b) if c1 != c2]
        return len(dif) == 2 and dif[0] == dif[1][::-1]
    
    def buddyStrings_own(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a, b = A, B
        if len(a) != len(b):
            return False
        c01, c02 = '', ''
        times = 0
        for c1, c2 in zip(a, b):
            if c1 != c2:
                if times > 1:
                    return False
                elif times == 1:
                    if c01 == c2 and c02 == c1:
                        times += 1
                    else:
                        return False
                else:
                    c01, c02 = c1, c2
                    times += 1
        if times == 0:
            return len(set(a)) < len(a)
        return times == 2
    
    def test(self):
        testCase = [
            ['ab', 'ba'],
            ['ab', 'ab'],
            ['aa', 'aa'],
            ['aaaaaabc', 'aaaaaacb'],
            ['', 'aa'],
        ]
        for a, b in testCase:
            res = self.buddyStrings(a, b)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
