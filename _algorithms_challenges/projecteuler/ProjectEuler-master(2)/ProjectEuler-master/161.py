import sys

class Grid():
    def __init__(self):
        self.n = None
        self.triomino_list = [
            [(0, 0), (1, 0), (0, 1)],
            [(0, 0), (1, 0), (1, 1)],
            [(0, 0), (0, 1), (1, 1)],
            [(0, 0), (1, 0), (1, -1)],
            [(0, 0), (0, 1), (0, 2)],
            [(0, 0), (1, 0), (2, 0)],
        ]

    def get(self, n):
        self.n = n
        start_grid = tuple(tuple(False for j in range(9)) for i in range(self.n))
        end_grid = tuple(tuple(True for j in range(9)) for i in range(self.n))
        counting = [{} for i in range(3 * self.n + 1)]
        counting[0][start_grid] = 1
        for i in range(3 * self.n):
            for top in counting[i]:
                empty_cell = self.__get_first_empty_cell(top)
                for triomino in self.triomino_list:
                    next_grid = self.__place_triomino(top, triomino, empty_cell)
                    if not next_grid:
                        continue
                    if next_grid not in counting[i + 1]:
                        counting[i + 1][next_grid] = 0
                    counting[i + 1][next_grid] += counting[i][top]
        return counting[3 * self.n][end_grid]

    def __get_first_empty_cell(self, grid):
        for i in range(self.n):
            for j in range(9):
                if not grid[i][j]:
                    return (i, j)
        return None

    def __place_triomino(self, grid, triomino, empty_cell):
        empty_cell_x, empty_cell_y = empty_cell
        for triomino_x, triomino_y in triomino:
            x = empty_cell_x + triomino_x
            y = empty_cell_y + triomino_y
            if x < 0 or x >= self.n or y < 0 or y >= 9:
                return None
            if grid[x][y]:
                return None
        result = [[False for j in range(9)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(9):
                result[i][j] = grid[i][j]
        for triomino_x, triomino_y in triomino:
            x = empty_cell_x + triomino_x
            y = empty_cell_y + triomino_y
            result[x][y] = True
        return self.__list_to_tuple(result)

    def __dump_grid(self, grid):
        if not grid:
            return
        print('+' + '-' * 9 + '+')
        for i in range(self.n):
            print('|' + ''.join(['*' if grid[i][j] else '.' for j in range(9)]) + '|')
        print('+' + '-' * 9 + '+')

    def __list_to_tuple(self, grid):
        return tuple(tuple(row) for row in grid)

    def __tuple_to_list(self, grid):
        return [list(row) for row in grid]

class Problem():
    def solve(self):
        for n in [2, 12]:
            print(n, '=>', self.get(n))

    def get(self, n):
        return Grid().get(n)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
