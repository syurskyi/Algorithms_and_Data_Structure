import sys

class RigidGraph():
    def __init__(self):
        self.mod = 1000000033
        self.c = None
        self.impl = None

    def S(self, dim):
        self._init_combination(dim)
        self._init_graph(dim)
        rv = 0
        for i in range(1, dim + 1):
            for j in range(1, dim + 1):
                rv += self.impl[i][j]
        return rv % self.mod

    def _init_combination(self, dim):
        self.c = [[0 for _ in range(dim + 1)] for _ in range(dim + 1)]
        self.c[0][0] = 1
        for i in range(1, dim + 1):
            self.c[i][0] = self.c[i][i] = 1
            for j in range(1, i):
                self.c[i][j] = self.c[i-1][j-1] + self.c[i-1][j]

    def _init_graph(self, dim):
        self.impl = [[None for _ in range(dim + 1)] for _ in range(dim + 1)]
        self.impl[0][1] = self.impl[1][0] = 1
        for m in range(2, dim + 1):
            self.impl[0][m] = self.impl[m][0] = 0
        for n in range(1, dim + 1):
            for m in range(1, n + 1):
                rv = 2**(m*n)
                for a in range(1, n + 1):
                    for b in range(m + 1):
                        if a == n and b == m:
                            continue
                        rv -= self.c[n - 1][a - 1] * self.c[m][b] * 2**((n-a) * (m-b)) * self.impl[a][b]
                rv %= self.mod
                self.impl[n][m] = self.impl[m][n] = rv
                print('R', n, m, '=>', rv)

class Problem():
    def solve(self):
        graph = RigidGraph()
        assert(graph.S(5) == 25021721)
        print(graph.S(100))

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
