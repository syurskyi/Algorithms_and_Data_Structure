import fractions
import itertools
import sys

class Problem():
    def __init__(self):
        self.__accumulated_sum = None
        self.__init__accumulated_sum()

    def __init__accumulated_sum(self):
        self.__accumulated_sum = [[[0 for c in range(24)] for b in range(24)] for a in range(24)]
        for a, b, c in itertools.product(range(24), repeat=3):
            result = self.get_multiple(a + 1, b + 1, c + 1)
            if a > 0:
                result += self.__accumulated_sum[a - 1][b][c]
            if b > 0:
                result += self.__accumulated_sum[a][b - 1][c]
            if c > 0:
                result += self.__accumulated_sum[a][b][c - 1]
            if a > 0 and b > 0:
                result -= self.__accumulated_sum[a - 1][b - 1][c]
            if b > 0 and c > 0:
                result -= self.__accumulated_sum[a][b - 1][c - 1]
            if c > 0 and a > 0:
                result -= self.__accumulated_sum[a - 1][b][c - 1]
            if a > 0 and b > 0 and c > 0:
                result += self.__accumulated_sum[a - 1][b - 1][c - 1]
            self.__accumulated_sum[a][b][c] = result

    def solve(self):
        self.sanity_check()

    def sanity_check(self):
        assert(self.get_multiple(4, 2, 5) == 6)
        assert(self.get_multiple_sum_naive(10) == 1972)
        assert(self.get_multiple_sum(10) == 1972)
        assert(self.get_multiple_sum_naive(30) == self.get_multiple_sum(30))
        assert(self.get_multiple_sum(10000) == 2024258331114)

    def get_multiple(self, a, b, c):
        gcd_list = [24, 6*a + 36, 6*a + 2*b + 14, a + b + c + 1]
        result = gcd_list[0]
        for i in range(1, len(gcd_list)):
            result = fractions.gcd(result, gcd_list[i])
        return result

    def get_multiple_sum_naive(self, n):
        result = 0
        for a, b, c in itertools.product(range(1, n + 1), repeat=3):
            result += self.get_multiple(a, b, c)
        return result

    def get_multiple_sum(self, n):
        q, r = divmod(n, 24)
        result = self.__accumulated_sum[23][23][23] * q**3
        if r > 0:
            result += self.__accumulated_sum[r - 1][r - 1][r - 1]
            result += self.__accumulated_sum[23][23][r - 1] * q**2
            result += self.__accumulated_sum[23][r - 1][23] * q**2
            result += self.__accumulated_sum[r - 1][23][23] * q**2
            result += self.__accumulated_sum[23][r - 1][r - 1] * q
            result += self.__accumulated_sum[r - 1][23][r - 1] * q
            result += self.__accumulated_sum[r - 1][r - 1][23] * q
        return result

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
