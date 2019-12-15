import sys

class Matrix():
    def multiply(self, x, y, mod):
        results = [[0 for j in range(len(y))] for i in range(len(x))]
        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                    results[i][j] = (results[i][j] + x[i][k] * y[k][j]) % mod
        return results

    def power(self, x, power, mod):
        base = x
        rv = self.identity_matrix(len(x))
        while power > 0:
            if power & 1 == 1:
                rv = self.multiply(rv, base, mod)
            base = self.multiply(base, base, mod)
            power >>= 1
        return rv

    def identity_matrix(self, n):
        rv = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            rv[i][i] = 1
        return rv

class Problem():
    def __init__(self):
        self.q = 10**9
        self.v = None
        self.transition_matrix = None
        self.__init_v()
        self.__init_transition_matrix()

    def solve(self):
        f = [self.get(13**i) for i in range(1, 17 + 1)]
        print(sum(f) % self.q)

    def get(self, n):
        if n < 10:
            return self.v[n + 1][0]
        x = Matrix().power(self.transition_matrix, n - 9, self.q)
        y = Matrix().multiply(x, self.v, self.q)[0][0]
        return y

    def __init_v(self):
        f_list = [0, 1]
        g_list = [0, 1]
        for i in range(2, 10):
            f = i
            g = 1
            for j in range(1, i):
                f += (10 * f_list[j] + (i - j) * g_list[j])
                g += g_list[j]
            f_list.append(f % self.q)
            g_list.append(g % self.q)
        self.v = [[x] for x in f_list[1:][::-1]] + [[x] for x in g_list[1:][::-1]]
        
    def __init_transition_matrix(self):
        self.transition_matrix = [[0 for j in range(18)] for i in range(18)]
        for j in range(9):
            self.transition_matrix[0][j] = 10
        for j in range(9, 18):
            self.transition_matrix[0][j] = j - 8
        for i in range(1, 9):
            self.transition_matrix[i][i - 1] = 1
        for j in range(9, 18):
            self.transition_matrix[9][j] = 1
        for i in range(10, 18):
            self.transition_matrix[i][i - 1] = 1

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
