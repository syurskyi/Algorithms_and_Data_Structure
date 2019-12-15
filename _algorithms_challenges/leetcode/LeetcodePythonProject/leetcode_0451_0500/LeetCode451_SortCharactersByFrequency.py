'''
Created on Apr 20, 2017

@author: MT
'''

class Solution(object):
    def frequencySort(self, s):
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        bucket = [[] for _ in range(len(s)+1)]
        for c, count in hashmap.items():
            bucket[count].append(c)
        result = ''
        for i in range(len(bucket)-1, -1, -1):
            while bucket[i]:
                c = bucket[i].pop()
                result += c*(i)
        return result
    
    def test(self):
        testCases = [
            'aaaa',
            'tree',
            'cccaaa',
            'Aabb',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.frequencySort(s)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()


