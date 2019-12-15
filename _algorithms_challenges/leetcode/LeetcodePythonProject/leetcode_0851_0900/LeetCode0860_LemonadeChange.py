'''
Created on Sep 15, 2019

@author: tongq
'''
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        hashmap = {
            5:0,
            10:0,
            20:0,
        }
        for b in bills:
            if b == 10:
                if hashmap[5] >= 1:
                    hashmap[5] -= 1
                else:
                    return False
            elif b == 20:
                val = 20
                if hashmap[10] >= 1:
                    hashmap[10] -= 1
                    val -= 10
                if val == 10:
                    if hashmap[5] >= 1:
                        hashmap[5] -= 1
                    else:
                        return False
                else:
                    if hashmap[5] >= 3:
                        hashmap[5] -= 3
                    else:
                        return False
            hashmap[b] += 1
        return True
    
    def test(self):
        testCases = [
#             [5,5,5,10,20],
            [5, 5, 10, 10, 20],
        ]
        for bills in testCases:
            res = self.lemonadeChange(bills)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
