import itertools
import sys

class Problem():
    def solve(self):
        total_count = 1
        for cycle in self.__generate_cycle():
            count = self.get_count(len(cycle))
            total_count *= count
        print(total_count)

    def get_count(self, cycle_length):
        zero_start_count = 1, 0
        one_start_count = 0, 1
        for i in range(cycle_length - 1):
            zero_start_count = zero_start_count[0] + zero_start_count[1], zero_start_count[0]
            one_start_count = one_start_count[0] + one_start_count[1], one_start_count[0]
        return (zero_start_count[0] + zero_start_count[1] + one_start_count[0])

    def __generate_cycle(self):    
        visited_input = set()
        for input in itertools.product([0, 1], repeat=6):
            if str(input) in visited_input:
                continue
            curr_state = input
            curr_cycle = []
            while str(curr_state) not in visited_input:
                visited_input.add(str(curr_state))
                curr_cycle.append(curr_state)
                a, b, c, d, e, f = curr_state
                curr_state = (b, c, d, e, f, a ^ (b & c))
            self.__assert_cycle(curr_cycle)
            yield curr_cycle

    def __assert_cycle(self, cycle):
        n = len(cycle)
        for i in range(n):
            curr_state = cycle[i]
            next_state = cycle[(i + 1) % n]
            assert(next_state[0] == curr_state[1])
            assert(next_state[1] == curr_state[2])
            assert(next_state[2] == curr_state[3])
            assert(next_state[3] == curr_state[4])
            assert(next_state[4] == curr_state[5])
            assert(next_state[5] == curr_state[0] ^ (curr_state[1] & curr_state[2]))

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
