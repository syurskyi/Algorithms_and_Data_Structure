'''
Created on Feb 18, 2017

@author: MT
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        hashset = set()
        if len(s) != len(t):
            return False
        for c1, c2 in zip(s, t):
            if c1 not in hashmap:
                if c2 in hashset:
                    return False
                hashmap[c1] = c2
                hashset.add(c2)
            else:
                if hashmap[c1] != c2:
                    return False
        return True
    
    def isIsomorphic_old(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        hashmap1, hashmap2 = {}, {}
        for c1, c2 in zip(s, t):
            if c1 in hashmap1 and\
            (c2 not in hashmap2 or hashmap1[c1] != c2 or hashmap2[c2] != c1):
                return False
            elif c2 in hashmap2 and\
            (c1 not in hashmap1 or hashmap1[c1] != c2 or hashmap2[c2] != c1):
                return False
            hashmap1[c1] = c2
            hashmap2[c2] = c1
        return True
    
    def test(self):
        testCases = [
            ('ab', 'aa'),
            ('egg', 'add'),
            ('foo', 'bar'),
            ('paper', 'title'),
        ]
        for s, t in testCases:
            print('s: %s, t: %s' % (s, t))
            result = self.isIsomorphic(s, t)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()