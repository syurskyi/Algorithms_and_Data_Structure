'''
Created on Apr 10, 2017

@author: MT
'''

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                prev = j
                while j+1 < len(abbr) and abbr[j+1].isdigit():
                    j+=1
                if abbr[prev:j+1].startswith('0'): return False
                num = int(abbr[prev:j+1])
                i += num
                j += 1
            else:
                if word[i] != abbr[j]:
                    return False
                i+=1
                j+=1
        if i != len(word) or j != len(abbr):
            return False
        return True
    
    def test(self):
        testCases = [
            ('internationalization', 'i12iz4n'),
            ('apple', 'a2e'),
        ]
        for word, abbr in testCases:
            print('word: %s' % word)
            print('abbr: %s' % abbr)
            result = self.validWordAbbreviation(word, abbr)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
