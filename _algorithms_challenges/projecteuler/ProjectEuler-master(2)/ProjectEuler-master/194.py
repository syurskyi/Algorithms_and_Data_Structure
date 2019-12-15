import math
import sys

class Problem():
    def solve(self):
        self.sanity_check()
        for a, b, c in [(25, 75, 1984)]:
            print(self.N(a, b, c) % 10**8)

    def sanity_check(self):
        assert(self.N(1, 0, 3) == 24)
        assert(self.N(0, 2, 4) == 92928)
        assert(self.N(2, 2, 3) == 20736)

    def N(self, a, b, c):
        assert(c >= 3)
        combination_ways = math.factorial(a + b) // math.factorial(a) // math.factorial(b)
        a_way = 2*(c-2)**2 + (c-2)*(c-3)**2 \
            + 2*(c-2)*((c-2)**2 + 2*(c-3)*(c-2) + (c-3)**3) \
            + (c-2)*(c-3)*(4*(c-3)*(c-2) + max(c-4, 0)*(c-3)**2)
        b_way = a_way + (c-2)*((c-3)*(c-1) + 2*(c-2)**2 + (c-3)**2*(c-2))
        return c * (c - 1) * combination_ways * a_way**a * b_way**b

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
