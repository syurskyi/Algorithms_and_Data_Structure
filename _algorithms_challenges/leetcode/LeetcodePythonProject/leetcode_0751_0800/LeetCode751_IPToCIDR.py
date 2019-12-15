'''
Created on Mar 26, 2018

@author: tongq
'''
class Solution(object):
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        x = 0
        ips= ip.split('.')
        for ip in ips:
            x = int(ip) + x*256
        res = []
        while n > 0:
            step = x &(-x)
            while step > n:
                step /= 2
            res.append(self.long2ip(x, step))
            x += step
            n -= step
        return res
    
    def long2ip(self, x, step):
        res = [0]*4
        for i in range(3, -1, -1):
            res[i] = x&255
            x >>= 8
        n = 33
        while step > 0:
            n -= 1
            step //= 2
        return '.'.join([str(s) for s in res])+'/'+str(n)
    
    def test(self):
        testCases = [
            [
                '255.0.0.7',
                10,
            ],
        ]
        for ip, n in testCases:
            result = self.ipToCIDR(ip, n)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
    
    for n in range(1, 20):
        print('n: %s' % n)
        print('{:b}'.format(n))
        print('{:b}'.format(-n))
        result = n&-n
        print('res: %s' % result)
        print('-='*30+'-')
