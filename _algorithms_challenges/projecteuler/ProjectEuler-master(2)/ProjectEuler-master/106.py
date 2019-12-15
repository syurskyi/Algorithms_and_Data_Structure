import itertools
import math
import sys

class Problem():
    def solve(self, n):
        needed_count = 0
        for set_size in range(2, n//2 + 1):
            for all_elements in itertools.combinations(range(n), 2*set_size):
                for first_elements in itertools.combinations(all_elements, set_size):
                    if first_elements[0] != all_elements[0]:
                        continue
                    first_set = list(first_elements)
                    second_set = list(set(all_elements) - set(first_set))
                    second_set.sort()
                    if self._is_needed(first_set, second_set):
                        needed_count += 1
        print(needed_count)
        
    def _is_needed(self, B, C):
        for i in range(len(B)):
            if B[i] > C[i]:
                return True
        return False
        
def main():
    problem = Problem()
    problem.solve(12)
    
if __name__ == '__main__':
    sys.exit(main())
