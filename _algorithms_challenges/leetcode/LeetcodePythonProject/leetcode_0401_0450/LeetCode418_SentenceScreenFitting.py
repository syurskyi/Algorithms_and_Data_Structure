'''
Created on Apr 12, 2017

@author: MT
'''

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        length = len(sentence)
        times = [0]*length
        nextInd = [0]*length
        for i in range(length):
            ind = i
            curLen = 0
            time = 0
            while curLen+len(sentence[ind])<=cols:
                curLen += len(sentence[ind])+1
                ind += 1
                if ind == len(sentence):
                    ind = 0
                    time += 1
            nextInd[i] = ind
            times[i] = time
        ind = 0
        res = 0
        for _ in range(rows):
            res += times[ind]
            ind = nextInd[ind]
        return res
    
    def test(self):
        testCases = [
            (["hello", "world"], 2, 8),
            (["a", "bcd", "e"], 3, 6),
            (["I", "had", "apple", "pie"], 4, 5),
        ]
        for sentence, rows, cols in testCases:
            print('sentence: %s' % sentence)
            print('rows: %s' % rows)
            print('cols: %s' % cols)
            result = self.wordsTyping(sentence, rows, cols)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
