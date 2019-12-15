import sys
from fractions import Fraction
        
class ReachableNumbersProblem():        
    def __init__(self):
        self.n = None
        self.digits = None
        self.reachable_integers = None
        
    def solve(self, n):
        self.n = n
        self.digits = [i+1 for i in range(self.n)]
        self.reachable_integers = {}
        for i in range(n):
            hash_value = self._hash(i, i+1)
            self.reachable_integers[hash_value] = set()
            self.reachable_integers[hash_value].add(Fraction(i+1))
        
        positive_reachable_integer_sum = 0
        final_set = self._get_reachable_integers(0, self.n)
        for final in final_set:
            if final.numerator > 0 and final.denominator == 1:
                print('Positive reachable integer =>', final)
                positive_reachable_integer_sum += final
        print(positive_reachable_integer_sum)
        
    def _get_reachable_integers(self, i, j):
        hash_value = self._hash(i, j)
        if hash_value in self.reachable_integers:
            return self.reachable_integers[hash_value]
        self.reachable_integers[hash_value] = set()
        
        concatenated = Fraction(''.join(map(str, self.digits[i:j])))
        self.reachable_integers[hash_value].add(concatenated)
        print('Concatenated', concatenated)
        for k in range(i+1, j):
            left_set = self._get_reachable_integers(i, k)
            right_set = self._get_reachable_integers(k, j)
            for left in left_set:
                for right in right_set:
                    self.reachable_integers[hash_value].add(left + right)
                    self.reachable_integers[hash_value].add(left - right)
                    self.reachable_integers[hash_value].add(left * right)
                    if right != 0:
                        self.reachable_integers[hash_value].add(left / right)
        return self.reachable_integers[hash_value]
                    
    def _hash(self, i, j):
        return "%d-%d" % (i, j)
    
def main():
    problem = ReachableNumbersProblem()
    problem.solve(9)
    
if __name__ == '__main__':
    sys.exit(main())
