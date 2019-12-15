import math
import sys

class BaseConverter():
    def convert_decimal(self, n, base):
        reversed_rep = []
        d = n
        while d:
            d, r = divmod(d, base)
            reversed_rep.append(r)
        return reversed_rep[::-1]

    def convert_rep(self, rep, base):
        result = 0
        for digit in rep:
            result = result * base + digit
        return result

class BinomialCoefficient():
    def __init__(self, prime):
        self.prime = prime
        self.base_values = self.__init_base_values(prime)
        self.cache_values = {}
        self.base_converter = BaseConverter()

    def __init_base_values(self, prime):
        curr = [1]
        result = [curr]
        for n in range(2, prime + 1):
            next = [1]
            for k in range(1, n - 1):
                next.append(curr[k - 1] + curr[k])
            next.append(1)
            curr = next
            result.append(curr)
        return result

    def get(self, m, n):
        if m not in self.cache_values:
            self.cache_values[m] = {}
        if n not in self.cache_values[m]:
            m_rep = self.base_converter.convert_decimal(m, self.prime)
            n_rep = self.base_converter.convert_decimal(n, self.prime)
            offset = len(m_rep) - len(n_rep)
            result = 1
            for i in range(len(n_rep)):
                m_i = m_rep[offset + i]
                n_i = n_rep[i]
                if m_i < n_i:
                    return 0
                result = (result * self.base_values[m_i][n_i]) % self.prime
            self.cache_values[m][n] = result
        return self.cache_values[m][n]

class EulerNumber():
    def __init__(self, prime):
        self.prime = prime
        self.binomial_coefficient = BinomialCoefficient(prime)
        self.factorial_mod = self.__init_factorial_mod(prime)

        self.values = { 0: (1, prime - 1) }

    def __init_factorial_mod(self, prime):
        result = [1]
        for i in range(1, prime):
            result.append((result[-1] * i) % prime)
        return result

    def get(self, n):
        if n not in self.values:
            a = self.__factorial_mod(n)
            b = -1
            for k in range(n):
                c = self.binomial_coefficient.get(n, k)
                a_k, b_k = self.get(k)
                a += c * a_k
                b += c * b_k             
                b -= c * self.__factorial_mod(n - k)
            self.values[n] = (a % self.prime, b % self.prime)
        return self.values[n]

    def __factorial_mod(self, n):
        if n >= self.prime:
            return 0
        return self.factorial_mod[n]

class ChineseRemainderTheorem():
    """
    Solve x = a_i (mod n_i) where n_i are coprime.
    """
    def solve(self, a_list, n_list):
        a = a_list[0]
        m = n_list[0]
        for i in range(1, len(n_list)):
            n = n_list[i]
            b = a_list[i]
            q = m * n
            (x, y) = self.__extended_gcd(m, n)
            root = (a + (b - a) * x * m) % q
            a, m = root, q
        return a

    def __extended_gcd(self, a, b):
        (x, y) = (0, 1)
        (last_x, last_y) = (1, 0)
        while b != 0:
            (q, r) = divmod(a, b);
            (a, b) = (b, r)
            (x, last_x) = (last_x - q * x, x)
            (y, last_y) = (last_y - q * y, y)
        return (last_x, last_y)

class Problem():
    def solve(self):
        print(self.get(10**9))

    def get(self, n):
        prime_list = [7, 11, 73, 101, 137]
        A_mod_list = []
        b_mod_list = []
        for prime in prime_list:
            print("curr prime =>", prime)
            euler_number = EulerNumber(prime)
            n_mod = (n - prime) % (prime * (prime - 1)) + prime if n >= prime else n
            print("n_mod =>", n_mod)
            A_mod, B_mod = euler_number.get(n_mod)
            print("A(n) and B(n) mod", prime, "=>", A_mod, B_mod)        
            A_mod_list.append(A_mod)
            b_mod_list.append(B_mod)
        theorem = ChineseRemainderTheorem()
        A = theorem.solve(A_mod_list, prime_list)
        B = theorem.solve(b_mod_list, prime_list)
        print("A(n) mod 77777777 =>", A)
        print("B(n) mod 77777777 =>", B)
        return (A + B) % 77777777

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
