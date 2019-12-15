'''
Created on Oct 29, 2017

@author: MT
'''
class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        hashset = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = [i, i, j, j]
                    grid[i][j] = 2
                    self.helper(grid, i, j, res)
                    keys = self.generateKeys(grid, res)
                    found = False
                    for key in keys:
                        if key in hashset:
                            found = True
                            break
                    if not found:
                        hashset.add(keys.pop())
                        count += 1
        return count
    
    def helper(self, grid, i, j, res):
        res[0] = min(res[0], i)
        res[1] = max(res[1], i)
        res[2] = min(res[2], j)
        res[3] = max(res[3], j)
        m, n = len(grid), len(grid[0])
        for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                grid[x][y] = 2
                self.helper(grid, x, y, res)
    
    def generateKeys(self, grid, res):
        hashset = set()
        up, down, left, right = res[0], res[1], res[2], res[3]
        subGrid = []
        for i in range(up, down+1):
            tmp = []
            for j in range(left, right+1):
                tmp.append(grid[i][j])
            subGrid.append(tmp)
        self.addRotationKeys(subGrid, hashset)
        return hashset
    
    def addRotationKeys(self, grid, hashset):
        grid1 = grid
        grid2 = grid[::-1]
        grid3 = [row[::-1] for row in grid]
        for grid in [grid1, grid2, grid3]:
            grid0 = grid
            for _ in range(4):
                m, n = len(grid0), len(grid0[0])
                newGrid = [[0]*m for _ in range(n)]
                for i in range(m):
                    for j in range(n):
                        newGrid[j][i] = grid0[i][j]
                hashset.add(self.getKey(newGrid))
                grid0 = newGrid
            for _ in range(4):
                m, n = len(grid0), len(grid0[0])
                newGrid = [[0]*m for _ in range(n)]
                for i in range(m):
                    for j in range(n):
                        newGrid[n-1-j][m-1-i] = grid0[i][j]
                hashset.add(self.getKey(newGrid))
                grid0 = newGrid
    
    def getKey(self, grid):
        return ','.join([''.join([str(num) for num in row]) for row in grid])
    
    def test(self):
        testCases = [
            [
                '11000',
                '10000',
                '00001',
                '00011',
            ],
            [
                '11100',
                '10001',
                '01001',
                '01110',
            ],
            [
                '0000111',
                '1111111',
                '0000000',
                '0000111',
                '1111110',
                '0001000',
            ],
            [
                '011',
                '111',
                '000',
                '111',
                '110',
            ],
            [
                '0111110110111111',
                '0000011111011101',
                '1010000100011101',
                '1111101000010011',
                '0100111111001111',
                '0101001001110100',
                '0001111100100001',
                '0111011010000001',
                '1101000100110110',
                '1101110011010010',
                '1010100011000010',
                '0011101101111100',
                '1100011101011111',
                '0001110101000101',
                '0101101000001011',
                '1100100101000110',
                '1100110010010010',
                '0111001011101010',
                '0100011001010100',
                '0101101010111100',
                '0101001110010001',
                '1101101100010000',
                '1001010000111111',
                '0001110100111100',
                '0011110001111000',
                '0001111111010000',
                '1111010001000010',
                '0111101110100110',
                '0011000111101111',
                '1101000110110100',
                '1001000110000001',
                '1100011111100001',
                '1010001000101110',
                '1100110000100011',
                '0010011010100011',
                '0011111011011001',
                '1100100100111101',
                '1011110110110011',
                '1001010111100011',
                '0100000010011110',
                '0110000100000000',
                '0010000100111110',
                '0000100111110010',
                '0011101000001111',
                '1000110101000001',
                '0110010000011101',
                '0111010110001111',
                '0001001101110110',
                '0010001101010110',
                '1000000101000110',
            ],
        ]
        for grid in testCases:
            print('grid:')
            grid = [[int(c) for c in row] for row in grid]
            print('\n'.join([str(row) for row in grid]))
            result = self.numDistinctIslands2(grid)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
