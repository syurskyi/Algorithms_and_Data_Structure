'''
Created on Oct 24, 2017

@author: MT
'''
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hashmap = {}
        for word in words:
            hashmap[word] = hashmap.get(word, 0)+1
        n = len(words)
        dp = [[] for _ in range(n+1)]
        for word, freq in hashmap.items():
            dp[freq].append(word)
        res = []
        for i in range(n, -1, -1):
            if dp[i]:
                dp[i].sort()
                res += dp[i]
                if len(res) >= k:
                    break
        return res[:k]
    
    def test(self):
        testCases = [
            [
                ["i", "love", "leetcode", "i", "love", "coding"],
                2,
            ],
            [
                ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
                4
            ],
        ]
        for words, k in testCases:
            print('words: %s' % words)
            print('k: %s' % k)
            result = self.topKFrequent(words, k)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
