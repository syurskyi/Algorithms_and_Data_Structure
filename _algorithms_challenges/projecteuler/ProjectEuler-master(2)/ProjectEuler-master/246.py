from fractions import Fraction
from math import sqrt
import sys

class QuadraticNumber():
    def __init__(self, a, b, d):
        self.a = a
        self.b = b
        self.d = d

    def __add__(self, other):
        assert(self.d == other.d)
        a = self.a + other.a
        b = self.b + other.b
        return QuadraticNumber(a, b, self.d)
 
    def __sub__(self, other):
        assert(self.d == other.d)
        a = self.a - other.a
        b = self.b - other.b
        return QuadraticNumber(a, b, self.d)

    def __mul__(self, other):
        assert(self.d == other.d)
        a = self.a * other.a + self.b * other.b * self.d
        b = self.a * other.b + self.b * other.a
        return QuadraticNumber(a, b, self.d)

    def __pow__(self, power):
        base = QuadraticNumber(self.a, self.b, self.d)
        result = QuadraticNumber(1, 0, self.d)
        while power > 0:
            if power & 1 == 1:
                result = result * base
            base = base * base
            power >>= 1
        return result

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.d == 0 or self.b == 0:
            return str(self.a)
        elif self.a == 0:
            return str(self.b) + " Sqrt[" + str(self.d) + "]"
        else:
            return str(self.a) + " + " + str(self.b) + " Sqrt[" + str(self.d) + "]"

class Ellipse():
    def __init__(self, a2, b2):
        self.a2 = a2
        self.b2 = b2

    def is_good_angle(self, pole):
        a2, b2 = self.a2, self.b2
        x0, y0 = pole
        d = b2 * x0**2 + a2 * y0**2 - a2 * b2
        denominator = b2 * x0**2 + a2 * y0**2

        # tangent points
        x1 = QuadraticNumber(Fraction(a2 * b2 * x0, denominator), Fraction(-a2 * y0, denominator), d)
        y1 = QuadraticNumber(Fraction(a2 * b2 * y0, denominator), Fraction( b2 * x0, denominator), d)
        x2 = QuadraticNumber(Fraction(a2 * b2 * x0, denominator), Fraction( a2 * y0, denominator), d)
        y2 = QuadraticNumber(Fraction(a2 * b2 * y0, denominator), Fraction(-b2 * x0, denominator), d)

        # pole
        x = QuadraticNumber(x0, 0, d)
        y = QuadraticNumber(y0, 0, d)
        
        # vectors from pole to two tangent points
        u = (x1 - x, y1 - y)
        v = (x2 - x, y2 - y)
        
        # check if angle => 45 degree        
        # angle >= 90 degree
        dot_product = self.__dot_product(u, v)
        assert(dot_product.b == 0)
        if dot_product.a < 0:
            return True
        lhs = self.__length2(u) * self.__length2(v)
        rhs = dot_product**2
        assert(lhs.b == 0)
        assert(rhs.b == 0)
        return lhs.a >= rhs.a * 2

    def __dot_product(self, u, v):
        return u[0] * v[0] + u[1] * v[1]

    def __length2(self, v):
        return v[0]**2 + v[1]**2

class Problem():
    def __init__(self):
        self.ellipse = None

    def solve(self):
        print(self.get(15000, 10000))

    def get(self, radius, locus_distance):
        self.ellipse = self.__build_ellipse(radius, locus_distance)
        a = radius // 2
        b = int(sqrt(((radius // 2)**2 - (locus_distance // 2)**2)))
        a2 = self.ellipse.a2
        b2 = self.ellipse.b2

        result = 0

        # positive x-axis
        x_at_boundary = self.__find_pole_at_boundary_with_fixed_y(0, a + 1, 20000)
        result += (x_at_boundary - a) * 2

        # positive y-axis
        y_at_boundary = self.__find_pole_at_boundary_with_fixed_x(0, b + 1, 20000)
        result += (y_at_boundary - b) * 2

        # quadrant i
        for y in range(1, b + 1):
            x_min = int(a * sqrt(1 - y**2 / b2))
            assert(b2 * x_min**2 + a2 * y**2 <= a2 * b2)
            assert(b2 * (x_min + 1)**2 + a2 * y**2 > a2 * b2)
            x_at_boundary = self.__find_pole_at_boundary_with_fixed_y(y, x_min + 1, 20000)
            result += (x_at_boundary - x_min) * 4
            print(result, "pole =>", (x_at_boundary, y), "ellipse boundary =>", x_min)
        for y in range(b + 1, y_at_boundary + 1):
            x_at_boundary = self.__find_pole_at_boundary_with_fixed_y(y, 1, 20000)
            result += x_at_boundary * 4
            print(result, "pole =>", (x_at_boundary, y))

        return result
        
    def __build_ellipse(self, radius, locus_distance):
        assert(radius % 2 == 0)
        assert(locus_distance % 2 == 0)
        a2 = (radius // 2)**2
        f2 = (locus_distance // 2)**2
        b2 = a2 - f2
        return Ellipse(a2, b2)

    def __find_pole_at_boundary_with_fixed_y(self, y, min_x, max_x):
        assert(self.ellipse.is_good_angle((min_x, y)))
        assert(not self.ellipse.is_good_angle((max_x, y)))
        while max_x - min_x > 1:
            x = (min_x + max_x) // 2
            if self.ellipse.is_good_angle((x, y)):
                min_x = x
            else:
                max_x = x
        return min_x

    def __find_pole_at_boundary_with_fixed_x(self, x, min_y, max_y):
        assert(self.ellipse.is_good_angle((x, min_y)))
        assert(not self.ellipse.is_good_angle((x, max_y)))
        while max_y - min_y > 1:
            y = (min_y + max_y) // 2
            if self.ellipse.is_good_angle((x, y)):
                min_y = y
            else:
                max_y = y
        return min_y        

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
