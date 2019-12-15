'''
Created on Mar 21, 2017

@author: MT
'''

class Solution(object):
    def reverseVowels(self, s):
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        if not s: return s
        s = list(s)
        left, right = 0, len(s)-1
        while left < right:
            while left < len(s) and s[left] not in vowels:
                left += 1
            while right >= 0 and s[right] not in vowels:
                right -= 1
            if left < right:
                s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)