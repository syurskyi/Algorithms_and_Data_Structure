import math
import sys

class ChineseRemainderTheorem():
    """
    Solve
        x = a (mod m)
        x = b (mod n)
    where m and n are coprime.
    """
    def solve(self, a, m, b, n):
        q = m*n
        (x, y) = self._extended_gcd(m, n)
        root = a + (b - a) * x * m
        return ((root % q) + q) % q
    
    def _extended_gcd(self, a, b):
        (x, y) = (0, 1)
        (last_x, last_y) = (1, 0)
        while b != 0:
            (q, r) = divmod(a, b);
            (a, b) = (b, r)
            (x, last_x) = (last_x - q * x, x)
            (y, last_y) = (last_y - q * y, y)
        return (last_x, last_y)

class ModInverse():
    """
    Solve ax = 1 (mod m).
    """
    def get(self, a, m):
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

class Problem():
    def __init__(self):
        self.theorem = ChineseRemainderTheorem()
        self.mod_inverse = ModInverse()
    
    def solve(self):
        for n in [9, 10, 20, 1000000000000]:
            print(n, self.get_last_nonzero_digits(n))

    def get_last_nonzero_digits(self, n, s=5):
        norm = self.get_norm(n, 5)
        a = self.get_last_factorial(n, 5, s)
        x = self.theorem.solve(a, 5**s, 0, 2**s)
        y = pow(self.mod_inverse.get(2, 5**s), norm, 5**s)
        return (x*y) % 10**s

    def get_last_factorial(self, n, p, s):
        result = 1
        t = 1
        i = 0
        while t <= n:
            result *= (-1)**(n // p**(s + i)) * self.get_free_factorial_naive((n // t) % p**s, p, s)
            result %= p**s
            t *= p
            i += 1
        return result

    def get_free_factorial_naive(self, n, p, s):
        result = 1
        mod = p**s
        for i in range(1, n + 1):
            if i % p != 0:
                result = (result * i) % mod
        return result

    def get_norm(self, n, p):
        t = p
        result = 0
        while t <= n:
            result += n // t
            t *= p
        return result

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
