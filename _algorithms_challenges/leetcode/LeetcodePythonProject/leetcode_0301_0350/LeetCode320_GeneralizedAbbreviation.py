'''
Created on Mar 17, 2017

@author: MT
'''

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.helper(word, 0, 0, '', res)
        return res
    
    def helper(self, word, i, count, curr, res):
        if i == len(word):
            if count:
                curr += str(count)
            res.append(curr)
            return
        self.helper(word, i+1, count+1, curr, res)
        if count:
            self.helper(word, i+1, 0, curr+str(count)+word[i], res)
        else:
            self.helper(word, i+1, 0, curr+word[i], res)
    
    def test(self):
        testCases = [
            'word',
        ]
        for word in testCases:
            print('word: %s' % (word))
            result = self.generateAbbreviations(word)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

