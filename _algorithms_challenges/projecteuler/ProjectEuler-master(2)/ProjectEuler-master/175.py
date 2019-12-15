import fractions
import sys

class Problem():
    def solve(self):
        print(self.get(fractions.Fraction(13, 17)))
        print(self.get(fractions.Fraction(123456789, 987654321)))
        
    def get(self, r):    
        calkin_wilf_tree_path = []
        m, n = r.denominator, r.numerator
        while m != 1 or n != 1:
            if m > n:
                m, n = m - n, n
                calkin_wilf_tree_path.append(1)
            elif m < n:
                m, n = m, n - m
                calkin_wilf_tree_path.append(0)
        calkin_wilf_tree_path.append(1)
        calkin_wilf_tree_path = calkin_wilf_tree_path[::-1] 
        return self.shorten(calkin_wilf_tree_path)
    
    def shorten(self, binary_expansion):
        rep = []
        last_digit, length_so_far = 1, 0
        for curr_digit in binary_expansion:
            if curr_digit == last_digit:
                length_so_far += 1
            else:
                rep.append(length_so_far)
                last_digit, length_so_far = curr_digit, 1
        rep.append(length_so_far)
        return ','.join(map(str, rep))
    
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
