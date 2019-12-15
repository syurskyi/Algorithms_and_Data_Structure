'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord(c)-ord('a')]+=1
            arr = [str(num) for num in arr]
            key = ''.join(arr)
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        res = []
        for value in hashmap.values():
            res.append(value)
        return res
    
    def test(self):
        pass

if __name__ == '__main__':
    Solution().test()
    