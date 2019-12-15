'''
Created on Sep 13, 2017

@author: MT
'''
class Excel(object):

    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        m = H
        n = ord(W)-ord('A')+1
        self.matrix = [[0]*n for _ in range(m)]
        self.hashmap = {}

    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        i = r-1
        j = ord(c)-ord('A')
        diff = v-self.matrix[i][j]
        self.matrix[i][j] = v
        for (i0, j0), vals in self.hashmap.items():
            self.matrix[i0][j0] += diff*(vals.count((i, j)))
        if (i, j) in self.hashmap:
            del self.hashmap[(i, j)]

    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        i, j = r-1, ord(c)-ord('A')
        return self.matrix[i][j]

    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        i, j = r-1, ord(c)-ord('A')
        for (i0, j0), vals in self.hashmap.items():
            if i0 == i and j0 == j:
                del self.hashmap[(i, j)]
                break
            for i1, j1 in vals:
                if i1 == i and j1 == j and (i, j) in self.hashmap:
                    del self.hashmap[(i, j)]
                    break
        vals = []
        sumVal = 0
        for s in strs:
            arr = s.split(':')
            if len(arr) == 1:
                x = int(arr[0][1:])-1
                y = ord(arr[0][0])-ord('A')
                vals.append((x, y))
                sumVal += self.matrix[x][y]
            else:
                x0 = int(arr[0][1:])-1
                y0 = ord(arr[0][0])-ord('A')
                x1 = int(arr[1][1:])-1
                y1 = ord(arr[1][0])-ord('A')
                for i0 in range(x0, x1+1):
                    for j0 in range(y0, y1+1):
                        vals.append((i0, j0))
                        sumVal += self.matrix[i0][j0]
        self.hashmap[(i, j)] = vals
        self.matrix[i][j] = sumVal
        return sumVal

if __name__ == '__main__':
    excel = Excel(3, 'C')
    excel.set(1, 'A', 2)
    print(excel.sum(3, 'C', ['A1', 'A1:B2']))
    excel.set(2, 'B', 2)
    print(excel.get(3, 'C'))
    print('-='*10+'-')
 
    excel = Excel(5, 'E')
    print(excel.get(1, 'A'))
    print(excel.set(1, 'A', 1))
    print(excel.get(1, 'A'))
    print(excel.sum(2, 'B', ['A1', 'A1']))
    print(excel.set(1, 'A', 2))
    print(excel.get(2, 'B'))
    print('-='*10+'-')
 
    excel = Excel(5, 'E')
    print(excel.set(1, 'A', 1))
    print(excel.sum(2, 'B', ['A1']))
    print(excel.set(2, 'B', 0))
    print(excel.get(1, 'B'))
    print(excel.set(1, 'A', 5))
    print(excel.get(2, 'B'))
    print('-='*10+'-')

    excel = Excel(3, 'C')
    print(excel.sum(1, 'A', ['A2']))
    print(excel.set(2, 'A', 1))
    print(excel.get(1, 'A'))
    print('-='*10+'-')
