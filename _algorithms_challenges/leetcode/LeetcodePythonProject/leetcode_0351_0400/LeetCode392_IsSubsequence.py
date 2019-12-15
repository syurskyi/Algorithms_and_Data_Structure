'''
Created on Apr 3, 2017

@author: MT
'''

class Solution(object):
    def isSubsequence(self, s, t):
        import bisect
        hashmap = {}
        for i, c in enumerate(t):
            if c in hashmap:
                hashmap[c].append(i)
            else:
                hashmap[c] = [i]
        prev = 0
        for i, c in enumerate(s):
            if c not in hashmap: return False
            j = bisect.bisect_left(hashmap[c], prev)
            if j == len(hashmap[c]): return False
            prev = hashmap[c][j]+1
        return True
    
    def isSubsequence_orig(self, s, t):
        import bisect
        idx = [[] for _ in range(256)]
        for i, c in enumerate(t):
            idx[ord(c)].append(i)
        prev = 0
        for i, c in enumerate(s):
            if idx[ord(c)] == []: return False
            j = bisect.bisect_left(idx[ord(c)], prev)
            if j == len(idx[ord(c)]): return False
            prev = idx[ord(c)][j] + 1
        return True
    
    def isSubsequence_slow(self, s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i < len(s):
            return False
        else:
            return True
    
    def test(self):
        testCases = [
            ('abc', 'ahbgdc'),
            ('axc', 'ahbgdc'),
        ]
        for s, t in testCases:
            print('s: %s' % s)
            print('t: %s' % t)
            result = self.isSubsequence(s, t)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

