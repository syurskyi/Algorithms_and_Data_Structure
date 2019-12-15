'''
Created on Aug 30, 2017

@author: MT
'''
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1: return False
        hashmap = {}
        for c in s1:
            hashmap[c] = hashmap.get(c, 0)+1
        left = 0
        hashmap0 = {}
        for i, c in enumerate(s2):
            if c in hashmap:
                while left < i and c in hashmap0 and hashmap0[c] >= hashmap[c]:
                    hashmap0[s2[left]] -= 1
                    left += 1
                hashmap0[c] = hashmap0.get(c, 0)+1
                if len(s1) == i-left+1:
                    return True
            else:
                left = i+1
                hashmap0 = {}
        return False
    
    def test(self):
        testCases = [
            ['ab', 'eidbaooo'],
            ['ab', 'eidboaoo'],
        ]
        for s1, s2 in testCases:
            print('s1: %s' % s1)
            print('s2: %s' % s2)
            result = self.checkInclusion(s1, s2)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
