import math
import sys

class TotientSummatoryFunction():
    def __init__(self, bound, mod):
        self.mod = mod
        self.small_values = None
        self.small_value_bound = None
        self.big_values = {}
        self.__init_small_values(bound)

    def __init_small_values(self, bound):
        n = 3 * int(math.pow(bound, 2 / 3))
        assert(n**3 >= bound**2)
        phi = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            if phi[i] != i:
                continue
            for j in range(i, n + 1, i):
                phi[j] = phi[j] // i * (i - 1)

        self.small_values = [0 for i in range(n + 1)]
        self.small_values[1] = phi[1] % self.mod
        for i in range(2, n + 1):
            self.small_values[i] = (self.small_values[i - 1] + phi[i]) % self.mod
        self.small_value_bound = n
        print("small_value_bound =>", self.small_value_bound)

    def get(self, n):
        if n <= self.small_value_bound:
            return self.small_values[n]
        
        if n not in self.big_values:
            result = n * (n + 1) // 2
            m = self.__int_sqrt(n)
            for d in range(1, m + 1):
                result -= self.get(d) * (n // d - n // (d + 1))
            for k in range(2, n // (m + 1) + 1):
                result -= self.get(n // k)
            self.big_values[n] = result % self.mod
            print("TotientSummatoryFunction get =>", n, self.big_values[n])
        return self.big_values[n]

    def __int_sqrt(self, n):
        guess = (n >> n.bit_length() // 2) + 1
        result = (guess + n // guess) // 2
        while abs(result - guess) > 1:
            guess = result
            result = (guess + n // guess) // 2
        while result * result > n:
            result -= 1
        return result

class Problem():
    def __init__(self):
        self.function = None
        self.cache = {}

    def solve(self):
        print(self.get([2, 3, 5, 7, 11, 13, 17], 10**11, 10**9))

    def get(self, n, m, mod):
        self.function = TotientSummatoryFunction(m, mod)
        for prime in n:
            self.cache[prime] = {}
        return self.S(n, m, mod)

    def S(self, n, m, mod):
        if n:
            p = n[0]
            q = n[1:]
            if m not in self.cache[p]:
                print("S =>", n, m, "=>", p, q)
                if m == 0:
                    self.cache[p][m] = 0
                else:
                    self.cache[p][m] = ((p - 1) * self.S(q, m, mod) + self.S(n, m // p, mod)) % mod
            return self.cache[p][m]
        else:
            return self.function.get(m)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

