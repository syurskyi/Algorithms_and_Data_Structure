import math
import sys

class Ellipse():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_unit_normal_vector(self, t):
        x0 = self.a * math.cos(t)
        y0 = self.b * math.sin(t)
        c = 1.0 / math.sqrt(x0**2 / self.a**4 + y0**2 / self.b**4)
        x = x0 + c * x0 / self.a**2
        y = y0 + c * y0 / self.b**2
        return x, y

    def get_volume(self):
        return 4 * math.pi / 3 * self.a**2 * self.b

class Problem():
    def solve(self):
        print(self.get(3, 1))

    def get(self, a, b, partition=2000000):
        ellipse = Ellipse(a, b)

        half_amount = 0.0
        x1, y1 = a + 1, 0
        delta_t = math.pi / 2 / partition
        for i in range(1, partition + 1):
            t = delta_t * i
            x2, y2 = ellipse.get_unit_normal_vector(t)
            delta_amount = math.pi / 3 * (x2**2 + x2 * x1 + x1**2) * (y2 - y1)
            half_amount += delta_amount
            x1, y1 = x2, y2

        chocolate_amount = 2 * half_amount - ellipse.get_volume()
        return chocolate_amount

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
