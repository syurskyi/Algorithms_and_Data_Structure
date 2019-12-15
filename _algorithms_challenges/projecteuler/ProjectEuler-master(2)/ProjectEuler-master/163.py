import itertools
import sys

class TriangleCounting():
    def get(self, n):
        # https://oeis.org/A210687
        return (1678 * n**3 + 3117 * n**2 + 88 * n - 345 * (n % 2) - 320 * (n % 3) - 90 * (n % 4) \
                - 288 * ((n**3 - n**2 + n) % 5)) // 240

    def get_naive(self, n):
        ABC_count = self.__get_ABC_triangles(n)
        ABD_count = self.__get_ABD_triangles(n)
        ABF_count = self.__get_ABF_triangles(n)
        ADF_count = self.__get_ADF_triangles(n)
        BDF_count = self.__get_BDF_triangles(n)
        DEF_count = self.__get_DEF_triangles(n)
        count = ABC_count + 6 * ABD_count + 3 * ABF_count + 6 * ADF_count + 3 * BDF_count + DEF_count
        return count
   
    def __get_ABC_triangles(self, n):
        return n * (n + 2) * (2 * n + 1) // 8

    def __get_ABD_triangles(self, n):
        count = 0
        for a, b, d in itertools.product(range(1, n + 1), range(1, n + 1), range(1, 2 * n)):
            if a + b >= n and a + d >= n and d - a <= n and b + d <= 2 * n and 2 * b + d >= 2 * n and a + 2 * b + d != 3 * n:
                count += 1
        return count

    def __get_ABF_triangles(self, n):
        # https://oeis.org/A212964
        return ((2 * n + 1) * (2 * n**2 + 2 * n - 3) + 3 * (-1)**n) // 24

    def __get_ABF_triangles_naive(self, n):
        count = 0
        for a, b, f in itertools.product(range(1, n + 1), range(1, n + 1), range(1, 2 * n)):
            if a + b >= n and a + f <= 2 * n and 2 * a + f >= 2 * n and b <= f and f <= 2 * b and a - b + f != n:
                count += 1
        return count

    def __get_ADF_triangles(self, n):
        count = 0
        for a, d, f in itertools.product(range(1, n + 1), range(1, 2 * n), range(1, 2 * n)):
            if a + d >= n and d - a <= n \
                    and a + f <= 2 * n and 2 * a + f >= 2 * n \
                    and f - d <= n and d + 2 * f >= 2 * n and 2 * d + f <= 4 * n \
                    and 3 * a + d + 2 * f != 5 * n:
                count += 1
        return count

    def __get_BDF_triangles(self, n):
        count = 0
        for b, d, f in itertools.product(range(1, n + 1), range(1, 2 * n), range(1, 2 * n)):
            if b <= d and d <= 2 * b \
                    and b <= f and f <= 2 * b \
                    and d <= 2 * f and f <= 2 * d and d + f <= 3 * n \
                    and 3 * b - d - f != 0:
                count += 1
        return count

    def __get_DEF_triangles(self, n):
        count = 0
        for d, e, f in itertools.product(range(1, 2 * n), repeat=3):
            if d - e <= n and e + 2 * d >= 2 * n and 2 * e + d <= 4 * n \
                    and e - f <= n and f + 2 * e >= 2 * n and 2 * f + e <= 4 * n \
                    and f - d <= n and d + 2 * f >= 2 * n and 2 * d + f <= 4 * n \
                    and d + e + f != 3 * n:
                count += 1
        return count

class Problem():
    def solve(self):
        for n in [1, 2, 36]:
            print(n, "=>", TriangleCounting().get(n))

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())