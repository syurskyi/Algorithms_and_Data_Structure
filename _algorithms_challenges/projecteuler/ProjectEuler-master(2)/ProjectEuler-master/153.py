import fractions
import sys

class Problem():
    def solve(self, n):
        rational_sum = self._rational_sigma_sum(n)
        print('Rational sum:', rational_sum)
        gaussian_sum = self._gaussian_sigma_sum(n)
        print('Gaussian sum:', gaussian_sum)
        print('Total sum:', rational_sum + gaussian_sum)
        
    def _rational_sigma_sum(self, n):
        rv = 0
        i = 1
        while i <= n:
            q = n // i
            min_i = n // (q+1)
            max_i = n // q
            rv += self._arithmetic_series_sum(min_i, max_i) * q
            i += (max_i - min_i)
        return rv    
    
    def _gaussian_sigma_sum(self, n):
        rv = 0
        i = 1
        while 2*i <= n:
            q = n // (2*i)
            min_i = n // (q+1) - n // (q+1) % 2
            max_i = n // q - n // q % 2
            rv += self._arithmetic_series_sum(min_i, max_i, 2) * q
            i += (max_i - min_i) // 2    
        
        for a in range(1, n+1):
            print('Current a =>', a)
            if a**2 > n:
                break
            for b in range(a+1, n+1):
                c = a**2 + b**2
                if c > n:
                    break
                if fractions.gcd(a, b) > 1:
                    continue
                i = 1
                while c*i <= n:
                    q = n // (c*i)
                    min_i = n // (q+1) - n // (q+1) % c
                    max_i = n // q - n // q % c
                    rv += self._arithmetic_series_sum(min_i // c, max_i // c) * q * 2 * (a + b)
                    i += (max_i - min_i) // c           
        return rv 
    
    def _arithmetic_series_sum(self, lower_bound, upper_bound, step=1):
        return (step + upper_bound) * (upper_bound // step) // 2 \
                - (step + lower_bound) * (lower_bound // step) // 2
    
def main():
    problem = Problem()
    problem.solve(5)
    problem.solve(10**5)
    problem.solve(10**8)
    
if __name__ == '__main__':
    sys.exit(main())
