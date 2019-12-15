'''
Created on Apr 11, 2017

@author: MT
'''

class Solution(object):
    def minAbbreviation(self, target, dictionary):
        diffs = []
        m = len(target)
        for word in dictionary:
            if len(word) != m: continue
            bits = 0
            for i, c in enumerate(word):
                if c != target[i]:
                    bits += 2**i
            diffs.append(bits)
        if not diffs:
            return str(m)
        abbrs = []
        for i in range(2**m):
            if all(d&i for d in diffs):
                abbrs.append(self.abbr(target, i))
        return min(abbrs, key=lambda x: len(x))
    
    def abbr(self, target, num):
        word, count = '', 0
        for w in target:
            if num & 1 == 1:
                if count:
                    word += str(count)
                    count = 0
                word += w
            else:
                count += 1
            num >>= 1
        if count:
            word += str(count)
        return word
    
    def test(self):
        testCases = [
            [
                "apple",
                ["blade"],
            ],
            [
                "apple",
                ["plain", "amber", "blade"],
            ],
        ]
        for target, dictionary in testCases:
            print('target: %s' % target)
            print('dictionary: %s' % dictionary)
            result = self.minAbbreviation(target, dictionary)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
