import fractions
import sys

class Problem():
    def solve(self):
        for n in [100, 100000]:
            print(n, self.get(n))

    def get(self, n):
        count = 0
        for a in range(1, n // 3 + 1):
            print(a, count)
            for b in range(a, (n - a) // 2 + 1):
                factor = (a + b) // fractions.gcd(a, b)
                q_first, r_first = divmod(b, factor)
                c_first = b
                if r_first != 0:
                    c_first = factor * (q_first + 1) 
                c_bound = min(a + b - 1, n - a - b)
                c_last = (c_bound // factor) * factor
                count += (c_last - c_first) // factor + 1
        return count

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
