import math
import sys

class Problem():
    def solve(self):
        self.p(3, 7)
        self.p(20000, 1000000)
        
    def p(self, k_defects, n_chips):
        max_double_defects = k_defects // 2
        good_counts = 0
        for n_double_defects in range(max_double_defects + 1):
            n_composite_defects = k_defects - n_double_defects
            good_counts += self.permutation_count(n_chips, n_composite_defects) * self.composite_count(k_defects, n_double_defects)
        print(1 - good_counts / n_chips**k_defects)

    def permutation_count(self, n, m):
        rv = 1
        for i in range(n - m + 1, n + 1):
            rv *= i
        return rv
            
    def composite_count(self, n_defects, n_double_defects):
        x = self.permutation_count(n_defects, n_double_defects * 2)
        return x // (2 ** n_double_defects) // math.factorial(n_double_defects)
    
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
