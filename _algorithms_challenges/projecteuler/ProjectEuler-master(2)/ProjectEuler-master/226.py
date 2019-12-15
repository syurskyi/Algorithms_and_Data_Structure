import math
import sys

class Problem():
    def __init__(self):
        self.epsilon = 1e-15
    
    def solve(self):
        p = self.find_intersection()
        q = 0.5
        print(self.integrate(p, q, 1e-5))

    def integrate(self, p, q, step):
        sum = 0.0
        x = p
        while x <= q:
            dy = self.blancmange_curve(x) - self.circle(x)
            sum += step * dy
            x += step
        return sum
    
    def find_intersection(self):
        # binary search on x in [0, 1/4].
        p = 0.0
        q = 0.25
        while abs(p - q) > self.epsilon:
            r = (p + q) * 0.5
            f = self.blancmange_curve(p) - self.circle(p)
            g = self.blancmange_curve(q) - self.circle(q)
            h = self.blancmange_curve(r) - self.circle(r)
            if f * h < 0.0:
                q = r
            elif g * h < 0.0:
                p = r
        return (p + q) * 0.5

    def circle(self, x):
        return 0.5 - math.sqrt(x * (0.5 - x))

    def blancmange_curve(self, x):
        y = 0.0
        n = 0
        while True:
            dy = self.s(2**n * x) / 2**n
            if dy < self.epsilon:
                break
            y += dy
            n += 1
        return y
    
    def s(self, x):
        n = int(x)
        return min(x - n, n + 1 - x)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
