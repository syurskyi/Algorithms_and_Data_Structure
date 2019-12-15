"""
    We are pleased to let you know that answer checking has now been restored to the website.
    Answer: 38788800
"""
import sys

class Problem():
    def __init__(self):
        self.mod = 76543217
    
    def solve(self):
        print(self.LC_mod(10, 5))
        print(self.LC_mod(10000, 5000))

    def LC_mod(self, m, n):
        assert(m == n * 2)
        rv = self._mod_factorial(m**2 - n**2, self.mod)
        for i in range(1, n + 1):
            rv *= self._mod_inverse(i**(2*i), self.mod)
            rv *= self._mod_inverse((i + m)**i, self.mod)
            rv %= self.mod
        for i in range(n + 1, m):
            rv *= self._mod_inverse(i**(2*(m - i)), self.mod)
            rv *= self._mod_inverse((i + m)**(m - i), self.mod)
            rv %= self.mod
        return rv

    def _mod_inverse(self, a, m):
        g, x, y = self._extended_gcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def _extended_gcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self._extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def _mod_factorial(self, n, m):
        rv = 1
        for i in range(1, n + 1):
            rv = (rv * i) % self.mod
        return rv

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
