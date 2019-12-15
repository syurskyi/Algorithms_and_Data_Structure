import math
import itertools
import sys

class PatternFactory():
    def build(self, n):
        for count_array in itertools.product(range(3), repeat=10):
            if sum(count_array) != 10:
                continue
            if sum([i * count_array[i] for i in range(10)]) == n:
                yield count_array

class Problem():
    def __init__(self):
        self.__factorial = [math.factorial(i) for i in range(11)]
        self.__factory = PatternFactory()

    def solve(self):
        result = 0
        for odd_position_sum in self.get_valid_odd_position_sum():
            curr_count = self.get_count(odd_position_sum)
            result += curr_count
            print(odd_position_sum, curr_count)
        print(result)

    def get_valid_odd_position_sum(self):
        for diff in [-44, -22, 0, 22, 44]:
            yield (90 + diff) // 2

    def get_count(self, odd_position_sum):
        result = 0
        for pattern in self.__factory.build(odd_position_sum):
            complement = [2 - count for count in pattern]
            odd_position_count = self.__count_odd_position(pattern)
            even_position_count = self.__count_even_position(complement)
            result += odd_position_count * even_position_count
        return result

    def __count_odd_position(self, pattern):
        result = self.__factorial[10]
        for count in pattern:
            result = result // self.__factorial[count]
        
        # ignore leading zero case
        leading_zero_result = 0
        if pattern[0] > 0:
            leading_zero_result = self.__factorial[9] // self.__factorial[pattern[0] - 1]
            for i in range(1, 10):
                leading_zero_result = leading_zero_result // self.__factorial[pattern[i]]
        return result - leading_zero_result

    def __count_even_position(self, pattern):
        result = self.__factorial[10]
        for count in pattern:
            result = result // self.__factorial[count]
        return result

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
