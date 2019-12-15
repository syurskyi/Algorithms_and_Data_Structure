import math
import sys

class Problem():
    def solve(self):
        for n in [5, 100, 10**12]:
            print(n, '=>', self.get(n))

    def get(self, n):
        total_sum = self.count(0, 0, 0, n) 
        print('x_0 = 0 =>', total_sum)

        total_sum += self.count(1, 1, 1, n - 1)
        print('x_0 = 1 =>', total_sum)

        sqrt_n = int(math.sqrt(n))
        for x_0 in range(2, sqrt_n + 1):
            total_sum += self.count(x_0, x_0, x_0, n // x_0)
        print('x_0 > 1 =>', total_sum)

        for x_0 in range(1, sqrt_n + 1):
            total_sum += self.count(-x_0, -x_0, 0, n // x_0)
        print('x_0 < 0, x_1 > 0 with <= Sqrt[n] =>', total_sum)

        for d in range(1, n // (sqrt_n + 1) + 1):
            total_sum += self.count(-(n // d), -(n // (d + 1)) - 1, 0, d)
        print('x_0 < 0, x_1 > 0 with > Sqrt[n] =>', total_sum)

        for x_0 in range(1, sqrt_n + 1):
            total_sum += self.count(-x_0, -x_0, -x_0, -1)
        print('x_0 < 0, x_1 < 0 with <= Sqrt[n] =>', total_sum)

        total_sum += self.count(-(n - 1), -(n // 2) - 1, -1, -1)
        for d in range(2, n // (sqrt_n + 1) + 1):
            total_sum += self.count(-(n // d), -(n // (d + 1)) - 1, -d, -1)
        print('x_0 < 0, x_1 < 0 with > Sqrt[n] =>', total_sum)

        return total_sum

    def count(self, x_0_first, x_0_last, x_1_first, x_1_last):
        line = self.count_under_line(x_0_first, x_0_last, x_1_first, x_1_last)
        parabola = self.count_under_parabola(x_0_first, x_0_last, x_1_first, x_1_last)
        return line - parabola

    def count_under_line(self, x_0_first, x_0_last, x_1_first, x_1_last):
        x_0_sigma_list = self.sigma_list(x_0_first, x_0_last)
        x_1_sigma_list = self.sigma_list(x_1_first, x_1_last)
        double_count = - x_0_sigma_list[3] * x_1_sigma_list[0] \
                + x_0_sigma_list[2] * x_1_sigma_list[1] \
                + x_0_sigma_list[2] * x_1_sigma_list[0] \
                - x_0_sigma_list[1] * x_1_sigma_list[2] \
                - 2 * x_0_sigma_list[1] * x_1_sigma_list[0] \
                + x_0_sigma_list[0] * x_1_sigma_list[3] \
                + x_0_sigma_list[0] * x_1_sigma_list[2] \
                + 2 * x_0_sigma_list[0] * x_1_sigma_list[1] \
                + 2 * x_0_sigma_list[0] * x_1_sigma_list[0]
        return double_count // 2

    def count_under_parabola(self, x_0_first, x_0_last, x_1_first, x_1_last):
        x_0_sigma_list = self.sigma_list(x_0_first, x_0_last)
        x_1_sigma_list = self.sigma_list(x_1_first, x_1_last)
        six_times_count = 2 * x_0_sigma_list[0] * x_1_sigma_list[3] \
                + 3 * x_0_sigma_list[0] * x_1_sigma_list[2] \
                + x_0_sigma_list[0] * x_1_sigma_list[1] \
                - 2 * x_0_sigma_list[3] * x_1_sigma_list[0] \
                + 3 * x_0_sigma_list[2] * x_1_sigma_list[0] \
                - x_0_sigma_list[1] * x_1_sigma_list[0]
        return six_times_count // 6
        
    def sigma_list(self, first, last):
        return [
            self.sigma_0(last) - self.sigma_0(first - 1),
            self.sigma_1(last) - self.sigma_1(first - 1),
            self.sigma_2(last) - self.sigma_2(first - 1),
            self.sigma_3(last) - self.sigma_3(first - 1),
        ]

    def sigma_0(self, n):
        return n

    def sigma_1(self, n):
        return n * (n + 1) // 2

    def sigma_2(self, n):
        return n * (n + 1) * (2 * n + 1) // 6

    def sigma_3(self, n):
        return (n * (n + 1) // 2)**2

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
