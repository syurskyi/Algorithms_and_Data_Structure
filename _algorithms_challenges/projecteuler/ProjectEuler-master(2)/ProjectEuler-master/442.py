import sys

class ElevenFreeInteger():
    def __init__(self, n):
        self.eleven_pattern_list = self.__init_eleven_pattern_list(n)
        self.prefix_list = self.__init_prefix_list()
        self.prefix_list_map = self.__init_prefix_list_map()
        self.dim = len(self.prefix_list) + 1
        self.transition_map = self.__init_transition_map()

        self.cache = {}

    def get(self, n):
        low = n
        high = 2 * n
        while low <= high:
            mid = (low + high) // 2
            x = mid - self.count(mid)
            print(mid, '=>', x)
            if x == n:
                return mid
            elif x > n:
                high = mid - 1
            else:
                low = mid + 1

    def count(self, n):
        result = 0
        n_literal = str(n)
        n_literal_len = len(n_literal)
        for i in range(n_literal_len):
            for digit in range(int(n_literal[i])):
                prefix = n_literal[:i] + str(digit)
                free_digit_count = n_literal_len - i - 1
                count = self.__count(prefix, free_digit_count)
                result += count
        if not self.__is_eleven_free(n):
            result += 1
        return result

    def __count(self, prefix, free_digit_count):
        if prefix not in self.cache:
            self.cache[prefix] = {}
        if free_digit_count not in self.cache[prefix]:
            count_vector = [0 for _ in range(self.dim)]
            count_vector[0] = 1
            for digit_literal in prefix:
                digit = int(digit_literal)
                next_count_vector = [0 for _ in range(self.dim)]
                for i in range(self.dim):
                    next_state = self.transition_map[i][digit]
                    next_count_vector[next_state] += count_vector[i]
                count_vector = next_count_vector

            for free_digit_pos in range(free_digit_count):
                next_count_vector = [0 for _ in range(self.dim)]
                for digit in range(10):
                    for i in range(self.dim):
                        next_state = self.transition_map[i][digit] 
                        next_count_vector[next_state] += count_vector[i]
                count_vector = next_count_vector
            self.cache[prefix][free_digit_count] = count_vector[-1]
        return self.cache[prefix][free_digit_count]

    def __init_eleven_pattern_list(self, max_length):
        result = []
        for i in range(1, max_length + 1):
            eleven_pattern = str(11**i)
            is_contained = False
            for existed in result:
                if existed in eleven_pattern:
                    is_contained = True
                    break
            if not is_contained:
                result.append(eleven_pattern)
        return result

    def __init_prefix_list(self):
        result = [''] # |''| means the initial state
        for pattern in self.eleven_pattern_list:
            for i in range(1, len(pattern)):
                prefix = pattern[:i]
                is_contained = False
                for existed in result:
                    if existed.startswith(prefix):
                        is_contained = True
                        break
                if not is_contained:
                    result.append(prefix)
        return result

    def __init_prefix_list_map(self):
        prefix_count = len(self.prefix_list)
        result = { None : prefix_count } # |None| means the final state
        for i in range(prefix_count):
            result[self.prefix_list[i]] = i
        return result

    def __init_transition_map(self):
        result = [[None for digit in range(10)] for i in range(self.dim)]
        for i in range(self.dim - 1):
            curr_state = self.prefix_list[i]
            for digit in range(10):
                next_state = self.__get_next_state(curr_state + str(digit))
                result[i][digit] = self.prefix_list_map[next_state]
        for digit in range(10):
            result[self.dim - 1][digit] = self.dim - 1
        return result

    def __is_eleven_free(self, n):
        n_literal = str(n)
        for eleven_pattern in self.eleven_pattern_list:
            if eleven_pattern in n_literal:
                return False
        return True

    def __get_next_state(self, pattern):
        if self.__is_finished(pattern):
            return None
        else:
            return self.__get_best_internal_state(pattern)

    def __is_finished(self, pattern):
        for eleven_pattern in self.eleven_pattern_list:
            if pattern.endswith(eleven_pattern):
                return True
        return False

    def __get_best_internal_state(self, pattern):
        internal_state_list = [prefix for prefix in self.prefix_list if pattern.endswith(prefix)]
        best_internal_state_list = []
        for state in internal_state_list:
            is_best = True
            for another in internal_state_list:
                if state != another and another.endswith(state):
                    is_best = False
                    break
            if is_best:
                best_internal_state_list.append(state)
        assert(len(best_internal_state_list) == 1)
        return best_internal_state_list[0]

class Problem():
    def __init__(self):
        self.eleven_free_integer = ElevenFreeInteger(18)

    def solve(self):
        #self.benchmark()
        print(self.eleven_free_integer.get(10**18))

    def benchmark(self):
        assert(self.eleven_free_integer.get(3) == 3)
        assert(self.eleven_free_integer.get(200) == 213)
        assert(self.eleven_free_integer.get(500000) == 531563)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

