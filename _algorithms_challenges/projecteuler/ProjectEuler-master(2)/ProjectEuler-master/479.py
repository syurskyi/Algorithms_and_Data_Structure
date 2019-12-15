import itertools
import sys

class Problem():
    def __init__(self):
        self.mod = 1000000007
    
    def solve(self):
        for n in [4, 10**6]:
            print(self.S_smart(n))

    def S(self, n):
        result = 0
        for k, p in itertools.product(range(1, n+1), repeat=2):
            result += (1 - k**2)**p
        return result % self.mod

    def S_smart(self, n):
        result = 0
        for k in range(1, n + 1):
            x = 1 - k**2
            result += x * (1 - pow(x, n, self.mod)) * self._mod_inverse(1 - x)
        return result % self.mod

    def _mod_inverse(self, a):
        g, x, y = self._extended_gcd(a, self.mod)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % self.mod

    def _extended_gcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self._extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
