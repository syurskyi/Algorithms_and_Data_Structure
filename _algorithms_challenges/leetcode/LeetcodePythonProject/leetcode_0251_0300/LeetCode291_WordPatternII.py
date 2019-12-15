'''
Created on Mar 8, 2017

@author: MT
'''

class Solution(object):
    def wordPatternMatch(self, pattern, s):
        if not pattern and not s: return True
        if not pattern or not s: return False
        hashmap = {}
        return self.helper(pattern, s, 0, 0, hashmap, set())
         
    def helper(self, pattern, s, i, j, hashmap, hashset):
        if i == len(pattern) and j == len(s):
            return True
        if i >= len(pattern) or j >= len(s):
            return False
        c = pattern[i]
        for k in range(j+1, len(s)+1):
            sub = s[j:k]
            if c not in hashmap and sub not in hashset:
                hashmap[c] = sub
                hashset.add(sub)
                if self.helper(pattern, s, i+1, k, hashmap, hashset):
                    return True
                del hashmap[c]
                hashset.remove(sub)
            elif c in hashmap and hashmap[c] == sub:
                if self.helper(pattern, s, i+1, k, hashmap, hashset):
                    return True
        return False
    
    def test(self):
        testCases = [
            ('abab', 'redblueredblue'),
            ('aaaa', 'asdasdasdasd'),
            ('aabb', 'xyzabcxzyabc'),
            ('d', 'ef'),
        ]
        for pattern, s in testCases:
            print('pattern: %s' % (pattern))
            print('s: %s' % (s))
            result = self.wordPatternMatch(pattern, s)
            print('result: %s' % (result))
            print('-='*20+'-')
    
if __name__ == '__main__':
    Solution().test()
