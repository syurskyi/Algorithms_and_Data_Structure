import sys

class Benchmark():
    def get(self, n, m, d):
        result = 0
        for k in range(d, m):
            c_nk = self.get_binomial_coefficient(n, k)
            c_kd = self.get_binomial_coefficient(k, d)
            result = result + c_nk * c_kd * (-1)**(k - d)
        return abs(result)

    def get_binomial_coefficient(self, n, m):
        if 2 * m > n:
            return self.get_binomial_coefficient(n, n - m)
        result = 1
        for i in range(m):
            result = result * (n - i) // (i + 1)
        return result

class BinomialCoefficient():
    def __init__(self):
        self.prime = 999999937
        self.mod_factorial = self.__init_mod_factorial()
        self.mod_inverse_factorial = self.__init_mod_inverse_factorial()

    def get(self, n, k):
        return (self.mod_factorial[n] \
            * self.mod_inverse_factorial[k] \
            * self.mod_inverse_factorial[n - k]) \
            % self.prime

    def get_pair(self, n, k, d):
        return (self.mod_factorial[n] \
            * self.mod_inverse_factorial[n - k] \
            * self.mod_inverse_factorial[k - d] \
            * self.mod_inverse_factorial[d]) \
            % self.prime

    def __init_mod_factorial(self):
        result = [1]
        for i in range(1, 630000 + 1):
            result.append((result[-1] * i) % self.prime)
        return result

    def __init_mod_inverse_factorial(self):
        result = [1]
        for i in range(1, 630000 + 1):
            result.append((result[-1] * self.__mod_inverse(i)) % self.prime)
        return result

    def __mod_inverse(self, a):
        g, x, y = self.__extended_gcd(a, self.prime)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % self.prime

    def __extended_gcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.__extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

class Problem():
    def solve(self):
        self.benchmark()
        print(self.get())

    def benchmark(self):
        print(Benchmark().get(6, 3, 1))
        print(Benchmark().get(100, 10, 4))

    def get(self):
        c = BinomialCoefficient()

        a_sum = 0
        for a in range(1000):
            a_sum = (a_sum + c.get(10000, a) * (-1)**a) % c.prime
        b_sum = 0
        for b in range(10000, 630000 + 1):
            b_sum = (b_sum + c.get_pair(630000, b, 10000) * (-1)**b) % c.prime

        a_rest_sum = c.get(10000, 1000)
        b_rest_sum = 0
        for b in range(10000, 63000):
            b_rest_sum = (b_rest_sum + c.get_pair(630000, b, 10000) * (-1)**b) % c.prime

        return c.prime - (a_sum * b_sum + a_rest_sum * b_rest_sum) % c.prime
    
def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
