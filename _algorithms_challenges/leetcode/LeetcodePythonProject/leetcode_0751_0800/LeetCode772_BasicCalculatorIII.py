'''
Created on Apr 5, 2018

@author: tongq
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        l1, o1 = 0, 1
        l2, o2 = 1, 1
        deque = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = ord(c)-ord('0')
                while i+1 < len(s) and s[i+1].isdigit():
                    i += 1
                    num = num*10+ord(s[i])-ord('0')
                l2 = l2*num if o2==1 else l2//num
            elif c == '(':
                deque.insert(0, l1)
                deque.insert(0, o1)
                deque.insert(0, l2)
                deque.insert(0, o2)
                l1, o1 = 0, 1
                l2, o2 = 1, 1
            elif c == ')':
                num = l1+o1*l2
                o2 = deque.pop(0)
                l2 = deque.pop(0)
                o1 = deque.pop(0)
                l1 = deque.pop(0)
                l2 = l2*num if o2 == 1 else l2//num
            elif c == '*' or c == '/':
                o2 = 1 if c=='*' else -1
            elif c == '+' or c == '-':
                l1 = l1 + o1*l2
                o1 = 1 if c=='+' else -1
                l2, o2 = 1, 1
            i += 1
        return l1+o1*l2
    
    def test(self):
        testCases = [
            "1 + 1",
            " 6-4 / 2 ",
            "2*(5+5*2)/3+(6/2+8)",
            "(2+6* 3+5- (3*14/7+2)*5)+3"
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.calculate(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
