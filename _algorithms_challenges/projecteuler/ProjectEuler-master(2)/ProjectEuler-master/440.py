import sys

class Matrix():
    def multiply(self, x, y, mod):
        results = [[0 for j in range(len(y[0]))] for i in range(len(x))]
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

class FibonacciSequence():
    def __init__(self):    
        self.q = 987898789
        self.f = [[1, 0]] # T(0) = 0, T(1) = 1
        self.transition_matrix = [[10, 1], [1, 0]] # T(n + 1) = 10 T(n) + T(n - 1)    
        self.cache = {}

    def get_power_list(self, n, max_power):
        result = []
        x = Matrix().power(self.transition_matrix, n, self.q)
        y = Matrix().multiply(x, self.f, self.q)[0][0]
        result.append(y)
        for i in range(max_power - 1):
            x = Matrix().power(x, n, self.q)
            y = Matrix().multiply(x, self.f, self.q)[0][0]
            result.append(y)
        return result

class Problem():
    def __init__(self):
        self.q = 987898789
        self.power_list = None
        self.power_frequency = None
        self.fibonacci_sequence = FibonacciSequence()

    def solve(self):
        self.benchmark()
        for n in [2000]:
            print('solution =>', n, '=>', self.get(n))

    def benchmark(self):
        assert(self.get(2) == 10444)
        assert(self.get(3) == 1292115238446807016106539989 % self.q)
        assert(self.get(4) == 670616280)

    def get(self, n):
        self.power_list = [[None for j in range(n + 1)] for i in range(n + 1)]
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                self.__init_power(a, b)

        self.power_frequency = {}
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                power = self.power_list[a][b]
                if power not in self.power_frequency:
                    self.power_frequency[power] = 0
                self.power_frequency[power] += 1

        result = self.power_frequency[-1] * ((n // 2) + (n + 1) // 2 * 10)
        for c in range(1, n + 1):
            print('current c =>', c)
            c_power_list = self.fibonacci_sequence.get_power_list(c, n)
            for power in range(1, n + 1):
                result += self.power_frequency[power] * c_power_list[power - 1] 
        return result % self.q

    def __init_power(self, a, b):
        if not self.power_list[a][b]:
            if a == b:
                self.power_list[a][b] = a
            if a == 0:
                self.power_list[a][b] = -1
            if a > b:
                self.power_list[a][b] = self.__init_power(b, a)
            else:
                self.power_list[a][b] = self.__init_power(abs(b - 2*a), a)
        return self.power_list[a][b]

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
