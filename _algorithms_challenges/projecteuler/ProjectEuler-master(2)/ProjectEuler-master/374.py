import math
import sys

class Problem():
    def __init__(self):
        self.mod = 982451653
    
    def solve(self):
        for n in [100, 10**14]:
            print(self.get_mod(n))

    def get_mod(self, n):
        mod_inverse_2 = self._mod_inverse(2)
        max_factorial, excluded_pos = self._get_boundary_case(n)
        print(max_factorial, excluded_pos)
        
        factorial_mod = [1, 2]
        acc_mod_inverse = 0
        excluded_acc_mod_inverse = 0
        sum = 3 # f(1) = 1, m(1) = 1, f(2) = 2, m(2) = 1

        for i in range(2, max_factorial + 1):
            factorial_mod = [factorial_mod[1], (factorial_mod[1] * (i+1)) % self.mod]
            acc_mod_inverse = (acc_mod_inverse +self._mod_inverse(i)) % self.mod
            
            if i == excluded_pos:
                excluded_acc_mod_inverse = acc_mod_inverse

            sum += factorial_mod[1] * acc_mod_inverse * (i - 1)
            sum += factorial_mod[0] * (i + 2) * mod_inverse_2 * (i - 1)
            sum += factorial_mod[1] * i
            if i % 100000 == 0:
                print(i, sum)

        excluded_sum = factorial_mod[1] * excluded_acc_mod_inverse * (max_factorial - 1)
        excluded_sum += factorial_mod[0] * (max_factorial + 2) * mod_inverse_2 * (max_factorial - 1)
        excluded_sum += factorial_mod[1] * max_factorial
        sum = (sum - excluded_sum) % self.mod
        return sum
            
    def _get_boundary_case(self, n):
        m = int((math.sqrt(8*n + 1) - 1) // 2)
        assert(m * (m+1) // 2 <= n)
        assert((m+1) * (m+2) // 2 > n)
        return m, m - (n - m * (m+1) // 2 + 1)
    
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
