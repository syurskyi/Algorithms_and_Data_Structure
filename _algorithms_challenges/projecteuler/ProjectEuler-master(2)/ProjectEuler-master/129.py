from fractions import Fraction
import math
import sys

class QuadraticInteger():
    def __init__(self, d, a, b):
        """
        Represents a + b sqrt[d] where d is square-free.
        """
        self.d = d
        self.a = a
        self.b = b
    
    def int(self):
        return self.a
    
    def __add__(self, other):
        return QuadraticInteger(self.d, self.a + other.a, self.b + other.b)
        
    def __sub__(self, other):
        return QuadraticInteger(self.d, self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        a = self.a * other.a + d * self.b * other.b
        b = self.a * other.b + self.b * other.a
        return QuadraticInteger(self.d, a, b)
    
    def __lt__(self, other):
        delta_a = self.a - other.a
        delta_b = other.b - self.b
        if delta_b == 0:
            return delta_a < 0
        elif delta_b > 0:
            x = delta_a / delta_b
            if x <= 0:
                return True
            else:
                return x**2 < self.d
        else:
            x = delta_a / delta_b
            if x <= 0:
                return False
            else:
                return x**2 > self.d

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __eq__(self, other):
        return (self.a == other.a) and (self.b == other.b)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return other.__lt__(self)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def inverse(self):
        x = self.a**2 - self.d * self.b**2
        return QuadraticInteger(self.d, Fraction(self.a, x), Fraction(-self.b, x))
    
    def floor(self):
        x = int(self.a + self.b * math.sqrt(self.d + 0.5))
        assert((x - self.a)**2 <= self.b**2 * self.d)
        assert(self.b**2 * self.d < (x + 1 - self.a)**2)
        return QuadraticInteger(self.d, x, 0)

    def abs(self):
        if self < QuadraticInteger(self.d, 0, 0):
            return QuadraticInteger(self.d, -self.a, -self.b)
        else:
            return QuadraticInteger(self.d, self.a, self.b)

    def value(self):
        return self.a + self.b * math.sqrt(self.d)

    def __str__(self):
        if self.b == 0:
            return str(self.a)
        else:
            return '%s + %s Sqrt[%s]' % (str(self.a), str(self.b), str(self.d))
    
    def __repr__(self):
        return self.__str__()

class ContinuedFraction():
    """
    Example: Sqrt[13] = [3; 1, 1, 1, 1, 6]
    """
    def sqrt(self, n, bound):
        if self._is_square(n):
            return None
        rep = self._get_rep(n)
        return self._get_best_approximation(n, rep, bound)
    
    def _get_rep(self, n):
        rep = []
        x = QuadraticInteger(n, 0, 1)
        visited = set()
        while str(x) not in visited:
            visited.add(str(x))
            integer_part = x.floor()
            rep.append(integer_part.int())
            x = (x - integer_part).inverse()
        return rep
    
    """
    http://en.wikipedia.org/wiki/Continued_fraction#Best_rational_approximations
    """
    def _get_best_approximation(self, n, rep, bound):
        repeated_len = len(rep) - 1
        P = [0, 1, rep[0]]
        Q = [1, 0, 1]
        i = 0
        while True:
            a_n = rep[i % repeated_len + 1]
            next_P = a_n * P[-1] + P[-2]
            next_Q = a_n * Q[-1] + Q[-2]
            if next_Q > bound:
                break
            i += 1
            P.append(next_P)
            Q.append(next_Q)
        
        best_fraction_so_far = P[-1], Q[-1]
        best_delta_so_far = QuadraticInteger(n, Fraction(P[-1], Q[-1]), -1).abs()
        for a in range(1, (bound - Q[-2]) // Q[-1] + 1):
            p = a * P[-1] + P[-2]
            q = a * Q[-1] + Q[-2]
            delta = QuadraticInteger(n, Fraction(p, q), -1).abs()
            if delta < best_delta_so_far:
                best_fraction_so_far = p, q
                best_delta_so_far = delta
        return best_fraction_so_far

    def _is_square(self, n):
        x = int(math.sqrt(n + 1))
        return x * x == n
    
class Problem():
    def solve(self):
        bound = 10**12
        denominator_sum = 0
        for n in range(2, 100000 + 1):
            rep = ContinuedFraction().sqrt(n, bound)
            if n % 1000 == 1:
                print(n, rep)
            if rep:
                denominator_sum += rep[1]
        print(denominator_sum)

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
