'''
Created on Sep 6, 2017

@author: MT
'''
class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.cmpStr = compressedString
        self.count = 0
        self.ind = 0
        if self.cmpStr:
            self.c = self.cmpStr[self.ind]
            self.ind += 1
            while self.ind < len(self.cmpStr) and self.cmpStr[self.ind].isdigit():
                self.ind += 1
            self.count = int(self.cmpStr[1:self.ind])

    def next(self):
        """
        :rtype: str
        """
        res = self.c
        self.count -= 1
        if self.count == 0:
            if self.ind == len(self.cmpStr):
                self.c = ' '
                return res
            self.c = self.cmpStr[self.ind]
            self.ind += 1
            ind = self.ind
            while ind < len(self.cmpStr) and self.cmpStr[ind].isdigit():
                ind += 1
            self.count = int(self.cmpStr[self.ind:ind])
            self.ind = ind
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.c != ' '

if __name__ == '__main__':
    it = StringIterator('L1e2t1C1o1d1e1')
    while it.hasNext():
        print(it.next())
