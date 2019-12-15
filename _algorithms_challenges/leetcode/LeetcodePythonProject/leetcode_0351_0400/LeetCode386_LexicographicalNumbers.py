'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object):
    def lexicalOrder(self, n):
        res = []
        curr = 1
        for _ in range(n):
            res.append(curr)
            if curr*10 <= n:
                curr *= 10
            elif curr%10 != 9 and curr+1 <= n:
                curr += 1
            else:
                while (curr//10)%10 == 9:
                    curr //= 10
                curr = curr//10+1
        return res
    
    def test(self):
        testCases = [
            113,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.lexicalOrder(n)
            print('result: %s' % result)
            print('-='*20+'-')

if __name__ == '__main__':
    Solution().test()
