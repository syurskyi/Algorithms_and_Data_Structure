import math
import sys

class TotientSummatoryFunction():
    def __init__(self, bound, mod):
        self.mod = mod
        self.phi = None
        self.small_values = None
        self.small_value_bound = None
        self.big_values = {}
        self.__init_small_values(bound)

    def __init_small_values(self, bound):
        n = 3 * int(math.pow(bound, 2 / 3))
        assert(n**3 >= bound**2)
        self.phi = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            if self.phi[i] != i:
                continue
            for j in range(i, n + 1, i):
                self.phi[j] = self.phi[j] // i * (i - 1)

        self.small_values = [0 for i in range(n + 1)]
        self.small_values[1] = self.phi[1] % self.mod
        for i in range(2, n + 1):
            self.small_values[i] = (self.small_values[i - 1] + i * self.phi[i]) % self.mod
        self.small_value_bound = n
        print("small_value_bound =>", self.small_value_bound)

    def get(self, n):
        if n <= self.small_value_bound:
            return self.small_values[n]
        
        if n not in self.big_values:
            result = n * (n + 1) * (2 * n + 1) // 6
            m = self.__int_sqrt(n)
            for d in range(1, m + 1):
                result -= self.get(d) * (self.__get_sum(n // d) - self.__get_sum(n // (d + 1)))
            for k in range(2, n // (m + 1) + 1):
                result -= (k * self.get(n // k))
            self.big_values[n] = result % self.mod
            print("TotientSummatoryFunction get =>", n, self.big_values[n])
        return self.big_values[n]

    def get_sum(self, n):
        result = 0
        m = self.__int_sqrt(n)
        for d in range(1, m + 1):
            result += d * (self.get(n // d) - self.get(n // (d + 1)))
        for k in range(1, n // (m + 1) + 1):
            result += (n // k) * k * self.phi[k]
        return result % self.mod

    def __int_sqrt(self, n):
        guess = (n >> n.bit_length() // 2) + 1
        result = (guess + n // guess) // 2
        while abs(result - guess) > 1:
            guess = result
            result = (guess + n // guess) // 2
        while result * result > n:
            result -= 1
        return result

    def __get_sum(self, n):
        return n * (n + 1) // 2

class ModInverse():
    """
    Solve ax = 1 (mod m).
    """
    def get(self, a, m):
        g, x, y = self.__extended_gcd(a, m)
        if g != 1:
            raise Exception("modular inverse does not exist")
        else:
            return x % m
    
    def __extended_gcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.__extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

class Problem():
    def solve(self):
        print(self.get(100, 999999017))
        print(self.get(99999999019, 999999017))

    def get(self, n, mod):
        function = TotientSummatoryFunction(n, mod)
        g = function.get_sum(n)
        y = ModInverse().get(2, mod)
        return ((g + n) * y) % mod

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

