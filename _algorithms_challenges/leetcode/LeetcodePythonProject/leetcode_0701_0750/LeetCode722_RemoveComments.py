'''
Created on Feb 19, 2018

@author: tongq
'''
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res = []
        isComment = False
        isLineComment = False
        line = ''
        for src in source:
            j = 0
            isLineComment = False
            while j < len(src):
                c = src[j]
                if j < len(src)-1 and src[j:j+2] == '//' and not isComment:
                    if line and not isComment:
                        res.append(line)
                    isLineComment = True
                    line = ''
                elif j < len(src)-1 and src[j:j+2] == '/*' and not isLineComment and not isComment:
                    j += 1
                    isComment = True
                elif j < len(src)-1 and src[j:j+2] == '*/' and isComment:
                    j += 1
                    isComment = False
                elif not isComment and not isLineComment:
                    line += c
                if j == len(src)-1 and not isComment:
                    if line:
                        res.append(line)
                    line = ''
                j += 1
        return res
    
    def test(self):
        testCases = [
            [
                "/*Test program */",
                "int main()", "{ ",
                "  // variable declaration ",
                "int a, b, c;",
                "/* This is a test",
                "   multiline  ",
                "   comment for ",
                "   testing */",
                "a = b + c;", "}",
            ],
            [
                "a/*comment",
                "line",
                "more_comment*/b",
            ],
            [
                "class test{",
                "public: ",
                "   int x = 1;",
                "   /*double y = 1;*/",
                "   char c;", "};"
            ],
            [
                "main() {",
                "/* here is commments",
                "  // still comments */",
                "   double s = 33;",
                "   cout << s;", "}"
            ],
            [
                "void func(int k) {",
                "// this function does nothing /*",
                "   k = k*2/4;",
                "   k = k/2;*/",
                "}",
            ],
            [
                "a//*b/*/c",
                "blank",
                "d/*/e/*/f"
            ],
            [
                "a/*/b//*c",
                "blank",
                "d//*e/*/f"
            ],
        ]
        for source in testCases:
            print('source: %s' % source)
            result = self.removeComments(source)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
