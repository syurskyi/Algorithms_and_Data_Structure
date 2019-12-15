import fractions
import sys

class GaussianEliminationAlgorithm():
    def __init__(self):
        self.cached = {}
    
    def solve(self, a, b):
        A = []
        for i in range(len(a)):
            row = list(a[i])
            row.append(b[i])
            A.append(row)
        hashed_A = str(A)
        if hashed_A not in self.cached:
            self.cached[hashed_A] = self.__gauss(A)
        return self.cached[hashed_A]
        
    def __gauss(self, A):
        n = len(A)
        for i in range(n):
            max_element = abs(A[i][i])
            max_row = i
            for k in range(i + 1, n):
                if abs(A[k][i]) > max_element:
                    max_element = abs(A[k][i])
                    max_row = k
            for k in range(i, n + 1):
                tmp = A[max_row][k]
                A[max_row][k] = A[i][k]
                A[i][k] = tmp
            for k in range(i+1, n):
                c = fractions.Fraction(-A[k][i], A[i][i])
                for j in range(i, n+1):
                    if i == j:
                        A[k][j] = 0
                    else:
                        A[k][j] += c * A[i][j]
        x = [0 for i in range(n)]
        for i in range(n-1, -1, -1):
            x[i] = fractions.Fraction(A[i][n], A[i][i])
            for k in range(i-1, -1, -1):
                A[k][n] -= A[k][i] * x[i]
        return x[0]

class Problem():
    def __init__(self):
        self.algorithm = GaussianEliminationAlgorithm()

    def solve(self):
        print("g(535) =>", self.get_g(535))
        print("sample =>", self.get(2, 999, 10**6))
        print("problem =>", self.get(2, 999999, 10**16))

    def get(self, lower_bound, upper_bound, constant):
        rv = 0
        for n in range(lower_bound, upper_bound + 1):
            g = self.get_g(constant // n)
            rv += g
            if n % 1000 == 0:
                print(n, constant // n, g)
        return rv

    def get_g(self, n):
        n_literal = str(n)
        matrix = self.__build_transition_matrix(n_literal)
        a, b = self.__build_linear_equations(matrix)
        return self.algorithm.solve(a, b) - len(n_literal) + 1

    def __build_transition_matrix(self, n):
        dim = len(n) + 1
        matrix = [[0 for _ in range(dim)] for _ in range(dim)]
        matrix[dim - 1][dim - 1] = 10
        for stage in range(dim - 1):
            for digit in range(10):
                next_pattern = n[:stage] + str(digit)
                for next_stage in range(stage + 1, -1, -1):
                    if next_pattern[stage + 1 - next_stage:] == n[:next_stage]:
                        matrix[stage][next_stage] += 1
                        break
        return matrix

    def __build_linear_equations(self, matrix):
        dim = len(matrix)
        a = [[0 for _ in range(dim)] for _ in range(dim)]
        b = [0 for _ in range(dim)]
        for i in range(dim):
            a[i][i] = 10
        for i in range(dim):
            for j in range(dim):
                a[i][j] -= matrix[i][j]
                cost = (i + 1 - j) * matrix[i][j]
                b[i] += cost
        a[dim - 1][dim - 1] = 1
        b[dim - 1] = dim - 1
        return a, b

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

