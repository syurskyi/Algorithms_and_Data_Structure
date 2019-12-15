'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object):
    def lengthLongestPath(self, input):
        maxLen = 0
        pathLen = {0:0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line)-len(name)
            if '.' in name:
                maxLen = max(maxLen, pathLen[depth]+len(name))
            else:
                pathLen[depth+1] = pathLen[depth]+len(name)+1
        return maxLen
    
    def test(self):
        testCases = [
#             'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext',
            'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n\tsubdir23\n\t\tsubsubdir23\n\t\t\tfile23.ext',
        ]
        for input in testCases:
            print('input:\n%s' % input)
            result = self.lengthLongestPath(input)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
