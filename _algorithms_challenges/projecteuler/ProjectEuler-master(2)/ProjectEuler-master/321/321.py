from fractions import Fraction
import sys

class QuadraticInteger():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self, other):
        return QuadraticInteger(self.a + other.a, self.b + other.b)
        
    def subtract(self, other):
        return QuadraticInteger(self.a - other.a, self.b - other.b)

    def multiply(self, other):
        a = self.a * other.a + 2 * self.b * other.b
        b = self.a * other.b + self.b * other.a
        return QuadraticInteger(a, b)
    
    def inverse(self):
        d = self.a**2 - 2*self.b**2
        return QuadraticInteger(Fraction(self.a, d), Fraction(-self.b, d))
    
    def power(self, n):
        if n == 0:
            return QuadraticInteger(1, 0)
        if n < 0:
            return self.power(-n).inverse()
        rv = QuadraticInteger(self.a, self.b)
        for i in range(1, n):
            rv = rv.multiply(self)
        return rv
    
    def __str__(self):
        return str(self.a) + ' + ' + str(self.b) + ' Sqrt[2]'
    
    def __repr__(self):
        return str(self.a) + ' + ' + str(self.b) + ' Sqrt[2]'
    
class Problem():
    def __init__(self):
        pass
        
    def solve(self):
        self.solve_by_conjecture()

    # Conjecture: M(n) = n(n+2)
    #    
    # So, n is a triangle number k(k+1)/2 
    # <=> n(n+2) = k(k+1)/2 
    # <=> 8(n+1)^2 - (2k+1)^2 = 7.
    # 
    # Then we use Wolfram Alpha to solve Diophantine equation.
    def solve_by_conjecture(self):
        n_array = []
        c_array = [
            [
                QuadraticInteger(Fraction(1, 2), Fraction(1, 8)), 
                QuadraticInteger(Fraction(-1, 2), Fraction(1, 8)), 
            ],
            [
                QuadraticInteger(Fraction(1, 2), Fraction(-1, 8)), 
                QuadraticInteger(Fraction(-1, 2), Fraction(-1, 8)), 
            ],
        ]
        d = [
            QuadraticInteger(3, 2), 
            QuadraticInteger(3, -2)
        ]
        for i in range(50):
            for c in c_array:
                m = c[0].multiply(d[0].power(i)).subtract(c[1].multiply(d[1].power(i)))
                assert(m.b == 0 and m.a.denominator == 1)
                n = m.a.numerator - 1
                if n > 0:
                    n_array.append(n)    
        n_array.sort()
        print(sum(n_array[:40]))
    
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
