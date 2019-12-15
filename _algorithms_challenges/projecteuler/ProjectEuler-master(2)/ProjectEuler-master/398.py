import fractions
import itertools
import sys

class Problem():
    def solve(self):
        print(self.get_expected_length(8, 3))
        print(self.get_expected_length(10**7, 100))

    def get_expected_length_naive(self, n, m):
        total_count = 0
        total_length_sum = 0
        for ropes in itertools.product(range(1, n - m + 1 + 1), repeat=m):
            if sum(ropes) == n:
                total_count += 1
                total_length_sum += sorted(ropes)[1]
        return fractions.Fraction(total_length_sum, total_count), total_length_sum, total_count

    def get_expected_length(self, n, m):
        total_count = self.__get_solution_count(m, n, 1)
        total_length_sum = 0
        second_shortest_length_bound = (n - 1) // (m - 1)
        for j in range(1, second_shortest_length_bound + 1):
            # shortest segment < second-shortest segment
            x = self.__get_solution_count(m, n - 1 - (m - 1) * j, 0) - self.__get_solution_count(m, n - 1 - (m - 1) * (j + 1), 0)
            y = self.__get_solution_count(m, n - j - (m - 1) * j, 0) - self.__get_solution_count(m, n - j - (m - 1) * (j + 1), 0)
            total_length_sum += j * (x - y) * m
                
            # shortest segment is equal to second-shortest segment
            for repeat_count in range(2, m + 1):
                if repeat_count * j > n: 
                    break
                solution_count = self.__get_solution_count(m - repeat_count, n - repeat_count * j, j + 1)
                total_length_sum += j * solution_count * self.__get_binomial_coefficient(m, repeat_count)

            # debug
            if j % 100 == 0:
                print("get_expected_length =>", j, total_length_sum, total_count)
        return total_length_sum / total_count, total_length_sum, total_count

    """
    Get the number of integer solution of x_1 + x_2 + ... + x_k = n, where x_i >= a.
    It is equivalent to (x_1 - a) + (x_2 - a) + ... + (x_k - a) = n - ka, or
    y_1 + y_2 + ... + y_k = n - ka, where y_i >= 0. 
    """
    def __get_solution_count(self, variable_count, total_sum, lower_bound):
        reduced_sum = total_sum - variable_count * lower_bound
        if reduced_sum == 0 and variable_count == 0:
            return 1
        return self.__get_binomial_coefficient(variable_count + reduced_sum - 1, reduced_sum)

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
