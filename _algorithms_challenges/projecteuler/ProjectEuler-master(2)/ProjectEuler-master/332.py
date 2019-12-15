import itertools
import math
import sys

class Problem():
    def solve(self):
        area_sum = 0.0
        for r in range(1, 51):
            area = self.A(r)
            area_sum += area
            print(r, area)
        print(area_sum)
        
    def A(self, r):
        points = self._get_lattice_points(r)
        min_area = 4 * math.pi * r**2
        for a, b, c in itertools.combinations(points, 3):
            try:
                area = self._get_area(r, a, b, c)
                if area > 1e-4:
                    min_area = min(min_area, area)
            except:
                pass
        return min_area
        
    def _get_lattice_points(self, r):
        points = []
        for x, y, z in itertools.product(range(-r, r+1), repeat=3):
            if x >= 0 and x**2 + y**2 + z**2 == r**2:
                points.append((x, y, z))
        return points
        
    def _get_area(self, r, a, b, c):
        angle_cab = self._get_angle(c, a, b)
        angle_abc = self._get_angle(a, b, c)
        angle_bca = self._get_angle(b, c, a)
        e = angle_cab + angle_abc + angle_bca - math.pi
        return e * r**2
            
    def _get_angle(self, c, a, b):
        cxa = self._cross_product(c, a)
        bxa = self._cross_product(b, a)
        numerator = self._inner_product(cxa, bxa)
        denominator = self._norm(cxa) * self._norm(bxa)
        return math.acos(numerator/denominator)
        
    def _cross_product(self, u, v):
        i = u[1] * v[2] - u[2] * v[1]
        j = u[2] * v[0] - u[0] * v[2]
        k = u[0] * v[1] - u[1] * v[0]
        return (i, j, k)
    
    def _inner_product(self, u, v):
        return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]
        
    def _norm(self, v):
        return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])
        
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
