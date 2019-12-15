import sys

class Problem():
    def __init__(self):
        self.found = None

    def solve(self):
        count = 0
        for digit in range(1, 10):
            solution_sum = self.s(digit) 
            print(digit, solution_sum)
            count += solution_sum
        print(count)
        
    def s(self, digit):
        self.found = []
        self.binary_search(1, 10**11, digit)
        return sum(self.found)
        
    def f(self, n, digit):
        count = 0
        factor = 1
        while n // factor != 0:
            lower_number = n - (n // factor) * factor
            curr_number = (n // factor) % 10
            higher_number = n // (factor * 10)
            if curr_number < digit:
                count += higher_number * factor
            elif curr_number == digit:
                count += higher_number * factor + lower_number + 1
            else:
                count += (higher_number + 1) * factor
            factor *= 10
        return count
    
    def binary_search(self, lower, upper, digit):
        if lower + 1 == upper:
            if self.f(lower, digit) == lower:
                self.found.append(lower)
            return
        middle = (lower + upper) // 2
        lower_value = self.f(lower, digit)
        upper_value = self.f(upper, digit)
        middle_value = self.f(middle, digit)
        if middle_value >= lower and middle >= lower_value:
            self.binary_search(lower, middle, digit)
        if upper_value >= middle and upper >= middle_value:     
            self.binary_search(middle, upper, digit)
        
    def f_naive(self, n, digit):
        return sum([self.count_naive(i, digit) for i in range(1, n+1)])
            
    def count_naive(self, n, digit):
        count = 0
        while n > 0:
            n, r = divmod(n, 10)
            if r == digit:
                count += 1
        return count
                    
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
