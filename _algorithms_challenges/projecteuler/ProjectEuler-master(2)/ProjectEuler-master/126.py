import sys

class Problem():
    def __init__(self):
        self.n_bound = 20000
        self.num_cubes = [0] * (self.n_bound + 1)

        self._init_num_cubes()
        
    def C(self, n):
        return self.num_cubes[n]
    
    def C_inverse(self, n):
        for i in range(1, self.n_bound + 1):
            if self.num_cubes[i] == n:
                return i
        return None
    
    def _init_num_cubes(self):
        for a in range(1, self.n_bound + 1):
            if 6*a*a > self.n_bound:
                break
            for b in range(a, self.n_bound + 1):
                if 2*b*(2*a+b) > self.n_bound:
                    break
                for c in range(b, self.n_bound + 1):
                    if 2*(a*b+b*c+c*a) > self.n_bound:
                        break
                    for layer in range(1, self.n_bound + 1):
                        num = self._num_cubes_on_layer(a, b, c, layer)
                        if num > self.n_bound:
                            break
                        self.num_cubes[num] += 1

    def _num_cubes_on_layer(self, a, b, c, layer):
        return 2*(a*b + b*c + c*a) + 4*(a + b + c + layer - 2)*(layer - 1)
        
def main():
    problem = Problem()
    for n, expected in zip([22, 46, 78, 118], [2, 4, 5, 8]):
        print(n, '=>', problem.C(n), expected)
    print(problem.C_inverse(10))
    print(problem.C_inverse(1000))
    
if __name__ == '__main__':
    sys.exit(main())
