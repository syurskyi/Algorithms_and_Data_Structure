'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path: return path
        result = ''
        if path.endswith('/'): path = path[:-1]
        if path.startswith('/'): path = path[1:]
        l = path.split('/')
        cont = 0
        for i in range(len(l)-1, -1, -1):
            if l[i] == '.' or l[i] == '':
                continue
            if l[i] == '..':
                cont += 1
                continue
            if cont > 0:
                cont -= 1
            else:
                result = '/' + l[i] + result
        if result == '':
            result = '/'
        return result
    
    def test(self):
        testCases = [
            '/home/',
            '/a/./b/../../c/',
        ]
        for path in testCases:
            print('path: %s' % path)
            result = self.simplifyPath(path)
            print('result: %s' % result)
            print('-='*15+'-')

if __name__ == '__main__':
    Solution().test()