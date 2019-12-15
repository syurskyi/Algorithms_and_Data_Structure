from math import sqrt
import sys

class Problem():
    def solve(self):
        k = 1 + 2 / sqrt(3)
        uncovered_area = 1 - 3 * (1/k)**2
        stack = [(-1, k, k), (k, -1, k), (k, k, -1), (k, k, k)]
        for i in range(10):
            next_stack = []
            for k1, k2, k3 in stack:
                k4 = self.get_k4(k1, k2, k3)
                next_stack += [(k1, k2, k4), (k2, k3, k4), (k3, k1, k4)]
                uncovered_area -= (1/k4)**2
            stack = next_stack
            print(uncovered_area)
        
    def get_k4(self, k1, k2, k3):
        return k1 + k2 + k3 + 2*sqrt(k1*k2 + k2*k3 + k3*k1)
        
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
