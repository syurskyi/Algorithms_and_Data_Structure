from sys import exit

class Problem():
    def solve(self):
        mod = 10**9
        m = [
            [1, 6, 0, 0, 0 ,0 ,0],
            [1, 1, 5, 0, 0, 0, 0],
            [1, 1, 1, 4, 0, 0, 0],
            [1, 1, 1, 1, 3, 0, 0],
            [1, 1, 1, 1, 1, 2, 0],
            [1, 1, 1, 1, 1, 1, 1],  
            [0, 0, 0, 0, 0, 0, 7],
        ]
        x = self.mod_pow(m, 10**12, mod)
        y = self.multiply(x, [[7], [0], [0], [0], [0], [0], [0]], mod)   
        print(y[0][0])

    def multiply(self, x, y, mod):
        rv = [[0 for j in range(len(y[0]))] for i in range(len(x))]
        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                    rv[i][j] = (rv[i][j] + x[i][k] * y[k][j]) % mod
        return rv

    def identity_matrix(self, n):
        rv = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            rv[i][i] = 1
        return rv

    def mod_pow(self, x, power, mod):
        base = x
        rv = self.identity_matrix(len(x))
        while power > 0:
            if power & 1 == 1:
                rv = self.multiply(rv, base, mod)
            base = self.multiply(base, base, mod)
            power >>= 1
        return rv

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    exit(main())