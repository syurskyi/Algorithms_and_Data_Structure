import sys

class Matrix():
    def __init__(self, entries):
        self.entries = entries

    def __mul__(self, other):
        result = [[0 for j in range(len(other.entries[0]))] for i in range(len(self.entries))]
        for i in range(len(self.entries)):
            for j in range(len(other.entries[0])):
                for k in range(len(other.entries)):
                    result[i][j] += self.entries[i][k] * other.entries[k][j]
        return Matrix(result)

    def __mod__(self, mod):
        if mod:
            for i in range(len(self.entries)):
                for j in range(len(self.entries[0])):
                    self.entries[i][j] %= mod
        return self

    def __pow__(self, n, mod=None):
        assert(n > 0)
        if n == 1:
            return self.__mod__(mod)
        half = self.__pow__(n >> 1, mod)
        if n & 1 == 1:
            return half.__mul__(half).__mul__(self).__mod__(mod)
        else:
            return half.__mul__(half).__mod__(mod)

    def __str__(self):
        return str(self.entries)

class LinearHomogeneousRecurrence():
    """
    Solve f(n+1) = c(n) f(n) + c(n-1) f(n-1) + ... + c(n-k) f(n-k) with
    f(0) = a(0), f(1) = a(1), ..., f(k) = a(k).
    
    Input:
        coefficients = [c(n), c(n-1), ..., c(n-k)]
        initial_values = [a(k), a(k-1), ..., a(0)]
    """
    def __init__(self, coefficients, initial_values):
        assert(len(coefficients) == len(initial_values))
        self.dim = len(coefficients)
        self.companion_matrix = self.__init__companion_matrix(coefficients)
        self.initial_state = self.__init__initial_state(initial_values)

    def __init__companion_matrix(self, coefficients):
        entries = [[0 for j in range(self.dim)] for i in range(self.dim)]
        for i in range(self.dim):
            entries[0][i] = coefficients[i]
        for i in range(1, self.dim):
            entries[i][i - 1] = 1
        return Matrix(entries)

    def __init__initial_state(self, initial_values):
        entries = [[value] for value in initial_values]
        return Matrix(entries)

    def get(self, n, mod=None):
        if n < self.dim:
            value = self.initial_state.entries[self.dim - n - 1][0]
            return value % mod if mod else value                 
        else:
            return ((pow(self.companion_matrix, n - self.dim + 1, mod) * self.initial_state) % mod).entries[0][0] 
            
class Problem():
    def solve(self):
        result = 0
        for i in range(1, 30 + 1):
            result = (result + self.get(i, 987654321, 10**8)) % 10**8
        print(result)

    def get(self, n, power, mod):
        recurrence = LinearHomogeneousRecurrence([2**n, 0, -n], [4**n, 2**n, 3])
        return recurrence.get(power, mod) - 1

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
