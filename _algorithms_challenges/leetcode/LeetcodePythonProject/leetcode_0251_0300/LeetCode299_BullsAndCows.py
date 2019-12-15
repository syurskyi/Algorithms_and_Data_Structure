'''
Created on Mar 9, 2017

@author: MT
'''

class Solution(object):
    def getHint(self, secret, guess):
        bulls = set()
        hashmap = {}
        for i, (c1, c2) in enumerate(zip(secret, guess)):
            if c1 == c2:
                bulls.add(i)
            else:
                hashmap[c1] = hashmap.get(c1, 0)+1
        cows = 0
        for i, c in enumerate(guess):
            if i not in bulls:
                if c in hashmap and hashmap[c] > 0:
                    hashmap[c] -= 1
                    cows += 1
        return '%sA%sB' % (len(bulls), cows)
    
    def test(self):
        testCases = [
            ('1807', '7810'),
            ('1123', '0111'),
        ]
        for secret, guess in testCases:
            print('secret: %s' % (secret))
            print('guess: %s' % (guess))
            result = self.getHint(secret, guess)
            print('result: %s' % (result))
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
