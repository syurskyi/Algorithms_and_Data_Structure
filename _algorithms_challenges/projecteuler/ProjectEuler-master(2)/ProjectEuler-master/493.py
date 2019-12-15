import itertools
import sys

class Problem():
    def solve(self):
        total_value_count = 0
        for color in range(2, 7 + 1):
            color_selection_count = self.__get_binomial_coefficient(7, color)
            for settings in itertools.product(range(1, 10 + 1), repeat=color):    
                if sum(settings) == 20:
                    value_count = 1
                    for i in settings:
                        value_count *= self.__get_binomial_coefficient(10, i)
                    total_value_count += value_count * color_selection_count * color
        sample_count = self.__get_binomial_coefficient(70, 20)
        print(total_value_count / sample_count, total_value_count, sample_count)

    def __get_binomial_coefficient(self, n, k):
        if k < 0 or n < 0 or n < k:
            return 0
        if k > n - k:
            return self.__get_binomial_coefficient(n, n - k)
        result = 1
        for i in range(k):
            result = result * (n - i) // (i + 1)
        return result
    
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
