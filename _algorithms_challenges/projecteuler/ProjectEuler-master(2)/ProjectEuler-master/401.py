import sys

class Problem():
    def __init__(self):
        self.modulo = 10**9
        
    def SIGMA2(self, n):
        sigma2 = 0
        i = 1
        while i <= n:
            q = n // i
            min_i = n // (q+1)
            max_i = n // q
            sigma2 += self.square_sum(min_i, max_i) * q
            sigma2 %= self.modulo
            i += (max_i - min_i)
        return sigma2
    
    def square_sum(self, a, b):
        return b*(b+1)*(2*b+1) // 6 - a*(a+1)*(2*a+1) // 6
    
def main():
    problem = Problem()
    print(problem.SIGMA2(10**15))
    
if __name__ == '__main__':
    sys.exit(main())
