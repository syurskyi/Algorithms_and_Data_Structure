import sys

class Problem():
    def solve(self):
        print(self.NF(61, 10**7))

    def N_mod(self, p, q, bound):    
        results = 0
        S = 290797
        for n in range(bound + 1):
            results += (S % p) * p**n
            S = (S**2) % 50515093
        return results
    
    def T(self, p, q):
        results = 0
        S = 290797
        for n in range(q + 1):
            results += (S % p)
            S = (S**2) % 50515093
        return results
        
    def NF(self, p, q):
        v = self.T(p, q)
        n = self.N_mod(p, q, 10)
        # 61**10 = 713342911662882601
        # https://www.wolframalpha.com/input/?i=Solve+60x+%3D+1+mod+713342911662882601
        return ((n - v) * 701453863135167891) % 713342911662882601
        
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())