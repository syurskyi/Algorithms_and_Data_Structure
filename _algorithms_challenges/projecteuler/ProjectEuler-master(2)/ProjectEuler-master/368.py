from decimal import getcontext, Decimal
from fractions import Fraction
import sys

class LUDecomposition():
    def __init__(self, A):
        self.LU = A.get_array_copy()
        self.m = A.m
        self.n = A.n
        self.pivot_sign = 1
        self.pivot_vector = [i for i in range(self.m)]

        LU_row_i = []
        LU_col_j = [0 for i in range(self.m)]
        for j in range(self.n):
            for i in range(self.m):
                LU_col_j[i] = self.LU[i][j]
            for i in range(self.m):
                LU_row_i = self.LU[i]
                s = sum([LU_row_i[k] * LU_col_j[k] for k in range(min(i, j))])
                LU_row_i[j] -= s
                LU_col_j[i] -= s

            p = j
            for i in range(j + 1, self.m):
                if abs(LU_col_j[i]) > abs(LU_col_j[p]):
                    p = i
            if p != j:
                for k in range(self.n):
                    self.LU[p][k], self.LU[j][k] = self.LU[j][k], self.LU[p][k]
                self.pivot_vector[p], self.pivot_vector[j] = self.pivot_vector[j], self.pivot_vector[p]
                self.pivot_sign = -self.pivot_sign
             
            if j < self.m and self.LU[j][j] != 0:
                for i in range(j + 1, self.m):
                    self.LU[i][j] *= Fraction(1, self.LU[j][j])

    def solve(self, B):
        assert(B.m == self.m)
        assert(self.nonsingular())

        X = B.get_submatrix(self.pivot_vector, 0, B.n - 1)
        for k in range(self.n):
            for i in range(k + 1, self.n):
                for j in range(B.n):
                    X.entries[i][j] -= self.LU[i][k] * X.entries[k][j]

        for k in range(self.n - 1, -1, -1):
            for j in range(B.n):
                X.entries[k][j] *= Fraction(1, self.LU[k][k])
            for i in range(k):
                for j in range(B.n):
                    X.entries[i][j] -= self.LU[i][k] * X.entries[k][j]
        return X

    def nonsingular(self):
        for j in range(self.n):
            if self.LU[j][j] == 0:
                return False
        return True



class Matrix():
    def identity(m, n):
        matrix = Matrix(m=m, n=n)
        for i in range(matrix.m):
            for j in range(matrix.n):
                if i == j:
                    matrix.entries[i][j] = 1
        return matrix

    def __init__(self, *args, **kwargs):
        self.entries = None
        self.m = None
        self.n = None
        if 'm' in kwargs and 'n' in kwargs and 'entries' not in kwargs:
            self.m = kwargs['m']
            self.n = kwargs['n']
            self.entries = [[0 for j in range(self.n)] for i in range(self.m)]
        elif 'm' not in kwargs and 'n' not in kwargs and 'entries' in kwargs:
            self.m = len(kwargs['entries'])
            self.n = len(kwargs['entries'][0])
            self.entries = kwargs['entries']

    def get_array_copy(self):
        copy = [[0 for j in range(self.n)] for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                copy[i][j] = self.entries[i][j]
        return copy

    def get_submatrix(self, row_index_array, begin_column_index, end_column_index):
        submatrix = Matrix(m=len(row_index_array), n=end_column_index - begin_column_index + 1)
        for i in range(len(row_index_array)):
            for j in range(begin_column_index, end_column_index + 1):
                submatrix.entries[i][j - begin_column_index] = self.entries[row_index_array[i]][j]
        return submatrix

    def minus(self, B):
        X = Matrix(m=self.m, n=self.n)
        for i in range(self.m):
            for j in range(self.n):
                X.entries[i][j] = self.entries[i][j] - B.entries[i][j]
        return X

    def times(self, scalar):
        X = Matrix(m=self.m, n=self.n)
        for i in range(self.m):
            for j in range(self.n):
                X.entries[i][j] = scalar * self.entries[i][j]
        return X

    def get_sum_of_entries(self):
        result = 0
        for i in range(self.m):
            for j in range(self.n):
                result += self.entries[i][j]
        return result

    def inverse(self):
        return self.solve(Matrix.identity(self.m, self.m))

    def solve(self, B):
        assert(self.m == self.n)
        return LUDecomposition(self).solve(B)



class KempnerSeries():
    def __init__(self, T):
        self.T = T
        self.n = len(T) - 1
        self.epsilon = Fraction(1, 10**20) 
        self.psi = []

    def get_sum(self):
        total_sum = self.get_one_digit_sum()
        total_sum += self.get_two_digits_sum()
        total_sum += self.get_more_digits_sum()
        total_sum += self.get_remaining_sum()
        return total_sum

    def get_one_digit_sum(self):
        result = 0
        for s in range(1, 10):
            if self.T[0][s]:
                result += Fraction(1, s)
        return result

    def get_two_digits_sum(self):
        k = 1
        while True:
            v = Matrix(m=self.n, n=1)
            for m1 in range(1, 10):
                for m2 in range(10):
                    i = self.T[0][m1]
                    if i and self.T[i][m2]:
                        s = m1 * 10 + m2
                        j = self.T[i][m2]
                        v.entries[j - 1][0] += Fraction(1, s**k)
            if k > 1 and v.get_sum_of_entries() < self.epsilon:
                break
            self.psi.append(v)
            k += 1
        return self.psi[0].get_sum_of_entries()

    def get_more_digits_sum(self):
        total_sum = 0
        i = 3
        while len(self.psi) > 1:
            k = 1
            while k <= len(self.psi):
                v = Matrix(m=self.n, n=1)
                for l in range(1, self.n + 1):
                    for m in range(10):
                        j = self.T[l][m]
                        if not j:
                            continue
                        for w in range(len(self.psi) - k + 1):
                            v.entries[j - 1][0] += self.get_coefficient_a(k, w, m) * self.psi[k - 1 + w].entries[l - 1][0]
                if k > 1 and v.get_sum_of_entries() < self.epsilon:
                    self.psi = self.psi[:k - 1]
                    break
                else:
                    self.psi[k - 1] = v
                k += 1
            total_sum += self.psi[0].get_sum_of_entries()
            i += 1
        return total_sum

    def get_remaining_sum(self):
        b = self.get_vector_b(self.get_matrix_B(self.get_matrix_A()))
        return self.inner_product(b, self.psi[0])

    def get_matrix_A(self):
        result = Matrix(m=self.n, n=self.n)
        for m in range(10):
            for l in range(1, self.n + 1):
                for j in range(1, self.n + 1):
                    if self.T[l][m] == j:
                        result.entries[j - 1][l - 1] += 1
        return result.times(Fraction(1, 10))
    
    def get_matrix_B(self, A):
        identity = Matrix.identity(m=self.n, n=self.n)
        return identity.minus(A).inverse().minus(identity)

    def get_vector_b(self, B):
        result = Matrix(m=self.n, n=1)
        for l in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                result.entries[l - 1][0] += B.entries[j - 1][l - 1]
        return result

    def get_coefficient_a(self, k, w, m):
        return Fraction(1, 10**(k + w)) * (-1)**w * self.get_binomial_coefficient(k + w - 1, w) * m**w

    def get_binomial_coefficient(self, n, m):
        if m > n - m:
            return self.get_binomial_coefficient(n, n - m)
        result = 1
        i, j = 1, n
        while i <= m:
            result *= Fraction(j , i)
            i, j = i + 1, j - 1
        return result
    
    def inner_product(self, A, B):
        assert(A.m == B.m)
        assert(A.n == 1)
        assert(B.n == 1)
        result = 0
        for i in range(A.m):
            result += A.entries[i][0] * B.entries[i][0]
        return result



class Problem():
    def __init__(self):
        getcontext().prec = 20

    def solve(self):
        #self.benchmark()
        self.get()

    def get(self):
        T = [ 
                [ 0, 2, 3, 4, 5, 6, 7, 8, 9, 10 ],
                [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 
                [ 1, 12, 3, 4, 5, 6, 7, 8, 9, 10 ],
                [ 1, 2, 13, 4, 5, 6, 7, 8, 9, 10 ], 
                [ 1, 2, 3, 14, 5, 6, 7, 8, 9, 10 ], 
                [ 1, 2, 3, 4, 15, 6, 7, 8, 9, 10 ], 
                [ 1, 2, 3, 4, 5, 16, 7, 8, 9, 10 ], 
                [ 1, 2, 3, 4, 5, 6, 17, 8, 9, 10 ], 
                [ 1, 2, 3, 4, 5, 6, 7, 18, 9, 10 ], 
                [ 1, 2, 3, 4, 5, 6, 7, 8, 19, 10 ],
                [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 20 ], 
                [ 0, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 
                [ 1, 0, 3, 4, 5, 6, 7, 8, 9, 10 ], 
                [ 1, 2, 0, 4, 5, 6, 7, 8, 9, 10 ],
                [ 1, 2, 3, 0, 5, 6, 7, 8, 9, 10 ],
                [ 1, 2, 3, 4, 0, 6, 7, 8, 9, 10 ],
                [ 1, 2, 3, 4, 5, 0, 7, 8, 9, 10 ],
                [ 1, 2, 3, 4, 5, 6, 0, 8, 9, 10 ],
                [ 1, 2, 3, 4, 5, 6, 7, 0, 9, 10 ],
                [ 1, 2, 3, 4, 5, 6, 7, 8, 0, 10 ],
                [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ], 
        ]
        print(self.rep(KempnerSeries(T).get_sum()))

    def benchmark(self):
        print('get_sum_with_no_digit_nine =>', self.get_sum_with_no_digit_nine())
        print('get_sum_with_no_even_digits =>', self.get_sum_with_no_even_digits())
        print('get_sum_with_no_odd_digits =>', self.get_sum_with_no_odd_digits())
        print('get_sum_with_no_42 =>', self.get_sum_with_no_42())
        print('get_sum_with_no_314 =>', self.get_sum_with_no_314())
        print('get_sum_with_no_even_digits_no_55_no_13579 =>', self.get_sum_with_no_even_digits_no_55_no_13579())

    def get_sum_with_no_digit_nine(self):
        T = [ 
                [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 0 ], 
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ],
        ]
        return self.rep(KempnerSeries(T).get_sum())

    def get_sum_with_no_even_digits(self):
        T = [ 
                [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 ],
                [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1 ],
        ]
        return self.rep(KempnerSeries(T).get_sum())

    def get_sum_with_no_odd_digits(self):
        T = [ 
                [ 0, 0, 1, 0, 1, 0, 1, 0, 1, 0 ],
                [ 1, 0, 1, 0, 1, 0, 1, 0, 1, 0 ],
        ]
        return self.rep(KempnerSeries(T).get_sum())

    def get_sum_with_no_42(self):
        T = [ 
                [ 0, 1, 1, 1, 2, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 2, 1, 1, 1, 1, 1 ],
                [ 1, 1, 0, 1, 2, 1, 1, 1, 1, 1 ],
        ]
        return self.rep(KempnerSeries(T).get_sum())

    def get_sum_with_no_314(self):
        T = [ 
                [ 0, 1, 1, 2, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 2, 1, 1, 1, 1, 1, 1 ],
                [ 1, 3, 1, 2, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 2, 0, 1, 1, 1, 1, 1 ],
        ]
        return self.rep(KempnerSeries(T).get_sum())

    def get_sum_with_no_even_digits_no_55_no_13579(self):
        T = [ 
                [ 0, 3, 0, 1, 0, 2, 0, 1, 0, 1 ],
                [ 0, 3, 0, 1, 0, 2, 0, 1, 0, 1 ],
                [ 0, 3, 0, 1, 0, 0, 0, 1, 0, 1 ],
                [ 0, 3, 0, 4, 0, 2, 0, 1, 0, 1 ],
                [ 0, 3, 0, 1, 0, 5, 0, 1, 0, 1 ],
                [ 0, 3, 0, 1, 0, 0, 0, 6, 0, 1 ],
                [ 0, 3, 0, 1, 0, 2, 0, 1, 0, 0 ],
        ]
        return self.rep(KempnerSeries(T).get_sum())

    def rep(self, fraction):
        return Decimal(fraction.numerator) / Decimal(fraction.denominator)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
