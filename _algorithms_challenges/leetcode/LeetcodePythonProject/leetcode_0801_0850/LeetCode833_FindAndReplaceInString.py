'''
Created on Jun 9, 2018

@author: tongq
'''
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        s = S
        prev = 0
        res = ''
        for ind, source, target in sorted(zip(indexes, sources, targets)):
            if s[ind:ind+len(source)] == source:
                res += s[prev:ind]
                res += target
                prev = ind + len(source)
        res += s[prev:]
        return res
    
    def test(self):
        testCases = [
            [
                "abcd",
                [0,2],
                ["a","cd"],
                ["eee","ffff"]
            ],
            [
                "abcd",
                [0,2],
                ["ab","ec"],
                ["eee","ffff"],
            ],
            [
                "vmokgggqzp",
                [3,5,1],
                ["kg","ggq","mo"],
                ["s","so","bfr"],
            ],
            [
                "imidcxiiqjwpvvcocjtskshvmqjnlhsqtezqttmoxuskbmujej",
                [35,6,22,40,17,19,12,2,42,4,8,45,14,29,47,24],
                ["qtt","ii","hv","xu","jt","sk","vv","id","skb","cx","qjw","mu","co","hsqtez","jej","mqjnl"],
                ["idl","vo","yl","pg","efp","vqi","s","wb","mw","gmt","rkqc","kdx","o","vamwgpn","pl","xyvz"],
            ],
        ]
        for s, indexes, sources, targets in testCases:
            res = self.findReplaceString(s, indexes, sources, targets)
            print('res: %s' % res)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
