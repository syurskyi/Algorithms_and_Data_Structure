'''
Created on Mar 19, 2017

@author: MT
'''

class Solution(object):
    def palindromePairs(self, words):
        if not words: return []
        hashmap = {}
        result = []
        for i, word in enumerate(words):
            hashmap[word] = i
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                s1 = word[:j]
                s2 = word[j:]
                if self.isPalindrome(s1):
                    str2rvs = s2[::-1]
                    if str2rvs in hashmap and hashmap[str2rvs] != i:
                        result.append([hashmap[str2rvs], i])
                if self.isPalindrome(s2):
                    str1rvs = s1[::-1]
                    if str1rvs in hashmap and hashmap[str1rvs] != i and s2:
                        result.append([i, hashmap[str1rvs]])
        return result
    
    def isPalindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True
    
    def test(self):
        testCases = [
            ["bat", "tab", "cat"],
            ["abcd", "dcba", "lls", "s", "sssll"],
        ]
        for words in testCases:
            print('words: %s' % (words))
            result = self.palindromePairs(words)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()

