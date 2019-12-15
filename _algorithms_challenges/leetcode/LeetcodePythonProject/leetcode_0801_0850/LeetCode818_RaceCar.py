'''
Created on May 1, 2018

@author: tongq
'''
class Solution(object):
    def __init__(self):
        self.hashmap = {0:0}
    
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target in self.hashmap: return self.hashmap[target]
        # Number of bits necessary to represent self in binary.
        n = target.bit_length()
        if 2**n-1 == target:
            self.hashmap[target] = n
        else:
            self.hashmap[target] = self.racecar(2**n-1-target)+n+1
            for m in range(n-1):
                self.hashmap[target] = min(self.hashmap[target],\
                            self.racecar(target-2**(n-1)+2**m)+n+m+1)
        return self.hashmap[target]
    
    def test(self):
        testCases = [
            3,
            6,
        ]
        for target in testCases:
            print('target: %s' % target)
            result = self.racecar(target)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
