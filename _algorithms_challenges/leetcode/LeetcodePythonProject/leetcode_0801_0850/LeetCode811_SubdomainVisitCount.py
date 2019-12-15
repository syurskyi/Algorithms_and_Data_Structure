'''
Created on Apr 25, 2018

@author: tongq
'''
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        hashmap = {}
        for s in cpdomains:
            cnt, s = s.split(' ')
            cnt = int(cnt)
            arr = s.split('.')[::-1]
            for i in range(1, len(arr)+1):
                s0 = '.'.join(arr[:i][::-1])
                hashmap[s0] = hashmap.get(s0, 0)+cnt
        res = []
        for s, freq in hashmap.items():
            res.append(str(freq) + ' ' + s)
        return res
    
    def test(self):
        testCases = [
            ["9001 discuss.leetcode.com"],
            ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
        ]
        for cpdomains in testCases:
            result = self.subdomainVisits(cpdomains)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
