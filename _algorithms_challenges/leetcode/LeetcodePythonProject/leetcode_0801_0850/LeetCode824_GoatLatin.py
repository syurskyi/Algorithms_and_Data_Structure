'''
Created on May 5, 2018

@author: tongq
'''
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = S
        vowels = set(list('aeiouAEIOU'))
        arr = s.split(' ')
        res = ''
        for i in range(len(arr)):
            if not arr[i]:
                continue
            word = arr[i]
            if word[0] not in vowels:
                word = word[1:]+word[0]
            word += 'ma'
            word += 'a'*(i+1)
            res += ' ' + word
        return res[1:]
    
    def test(self):
        testCases = [
            'I speak Goat Latin',
            'The quick brown fox jumped over the lazy dog',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.toGoatLatin(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
