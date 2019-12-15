import sys

class Matrix():
    def multiply(self, x, y, mod):
        results = [[0 for j in range(len(y[0]))] for i in range(len(x))]
        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                    results[i][j] = (results[i][j] + x[i][k] * y[k][j]) % mod
        return results

    def power(self, x, n, mod):
        if n == 1:
            return x
        half = self.power(x, n >> 1, mod)
        if n & 1 == 1:
            return self.multiply(self.multiply(half, half, mod), x, mod)
        else:
            return self.multiply(half, half, mod)

class FibonacciNumber():
    def __init__(self):
        self.matrix = Matrix()
    
    def get(self, n, mod):
        if n == 0:
            return 0
        if n == 1:
            return 1
        transition_matrix = [[0, 1], [1, 1]]
        return self.matrix.power(transition_matrix, n - 1, mod)[1][1]

class Problem():
    def __init__(self):
        self.fibonacci_number = FibonacciNumber()
    
    def solve(self):
        results = 0
        n = 10**15
        for x in range(1, 101):
            denominator = x**2 + x - 1
            mod = 1307674368000 * denominator
            numerator = (self.fibonacci_number.get(n+1, mod) * pow(x, n+1, mod) \
                    + self.fibonacci_number.get(n, mod) * pow(x, n+2, mod) - x) % mod
            assert(numerator % denominator == 0)
            results = (results + numerator // denominator) % 1307674368000
        print(results)

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
