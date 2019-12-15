import fractions
import math
import sys

class Problem():
    def solve(self):
        for r in [1053779]:
            print(self.T(r))

    def sanity_check(self):
        assert(self.T(100) == 1234)
        assert(self.T(1000) == 22767)
        assert(self.T(10000) == 359912)

    def T(self, r):
        total_count = 0
        performance_counter = 0
        bound = int(2 * r * math.sqrt(3))
        print('r:', r)
        print('bound:', bound)
        for m in range(1, bound + 1):
            for n in range(1, m):
                if m * n > bound:
                    break
                if fractions.gcd(m, n) != 1:
                    continue
                a = (m + 2 * n) * m
                b = (n + 2 * m) * n
                c = m * m + m * n + n * n
                g = 3 if (m - n) % 3 == 0 else 1
                total_count += int(r * g * 2 / (math.sqrt(3) * m * n))
                performance_counter += 1
                if performance_counter % 100000 == 0:
                    print(performance_counter, m, n, a, b, c, total_count)
        return total_count

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
