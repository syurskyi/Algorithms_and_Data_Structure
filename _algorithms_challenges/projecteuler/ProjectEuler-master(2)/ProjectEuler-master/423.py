import math
import sys

class ExtendedGCD():
    def solve(a, b):
        x, y = 0, 1
        last_x, last_y = 1, 0
        while b != 0:
            q, r = divmod(a, b)
            a, b = b, r
            x, last_x = last_x - q * x, x
            y, last_y = last_y - q * y, y
        return last_x, last_y

# Solve ax = 1 (mod m).
class ModInverse():
    def solve(a, m):
        x, y = ExtendedGCD.solve(a, m)
        return x % m

class Primes():
    def get(n):
        visited = [False for _ in range(n + 1)]
        m = int(math.sqrt(n))
        for i in range(2, m + 1):
            if not visited[i]:
                for j in range(i**2, n + 1, i):
                    visited[j] = True
        return [i for i in range(2, n + 1) if not visited[i]]

class Problem():
    def __init__(self):
        self.mod = 1000000007
        self.factorial = None
        self.inverse_factorial = None

    def solve(self):
        assert(self.get(50) == 832833871)
        print(self.get(50000000))
        
    def get(self, n):
        self.factorial = self.__set_factorial(n)
        self.inverse_factorial = self.__set_inverse_factorial(n)
        inverse_4 = ModInverse.solve(4, self.mod)
        extended_primes = [1] + Primes.get(n)
        extended_primes_len = len(extended_primes)
        print('Extended prime size =>', extended_primes_len)

        s = ((pow(5, n, self.mod) - 1) * inverse_4) % self.mod
        #print(s)
        result = s
        for c in range(1, extended_primes_len):
            curr_p = extended_primes[c]
            prev_p = extended_primes[c - 1]
            x = pow(5, n - c, self.mod) * self.get_binomial(n, c) - pow(5, curr_p - 1 - c, self.mod) * self.get_binomial(curr_p - 1, c)
            for i in range(prev_p, curr_p, 1):
                x += pow(5, i - c, self.mod) * self.get_binomial(i - 1, c - 1)
            s = ((x - s) * inverse_4) % self.mod
            result += s
        result = (6 * result) % self.mod
        print(result)
        return result

    def get_binomial(self, n, m):
        return (self.factorial[n] * self.inverse_factorial[m] * self.inverse_factorial[n - m]) % self.mod

    def __set_factorial(self, n):
        d = 1
        result = [d]
        for i in range(1, n + 1):
            d = (d * i) % self.mod
            result.append(d)
        return result

    def __set_inverse_factorial(self, n):
        d = 1
        result = [d]
        for i in range(1, n + 1):
            d = (d * ModInverse.solve(i, self.mod)) % self.mod
            result.append(d)
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
