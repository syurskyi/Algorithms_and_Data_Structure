'''
Created on Sep 11, 2019

@author: tongq
'''
class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        a, b = A, B
        if a == b:
            return 0
        q = [a]
        hashset = set([a])
        res = 0
        while q:
            res += 1
            size = len(q)
            for _ in range(size):
                s = q.pop(0)
                i = 0
                while s[i] == b[i]:
                    i += 1
                for j in range(i+1, len(s)):
                    if s[j] == b[j] or s[i] != b[j]:
                        continue
                    tmp = self.swap(s, i, j)
                    if tmp == b:
                        return res
                    if tmp not in hashset:
                        hashset.add(tmp)
                        q.append(tmp)
        return res
    
    def swap(self, s, i, j):
        l = list(s)
        l[i], l[j] = l[j], l[i]
        return ''.join(l)
    
    def test(self):
        testCases = [
            [
                'ab',
                'ba',
            ],
            [
                'abc',
                'bca',
            ],
            [
                'abac',
                'baca',
            ],
            [
                'aabc',
                'abca',
            ],
            [
                'abccab',
                'abccab',
            ],
        ]
        for a, b in testCases:
            res = self.kSimilarity(a, b)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
