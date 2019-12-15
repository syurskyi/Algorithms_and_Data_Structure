import sys

class PseudoRandomNumberGenerator():
    def get_period(self):
        return 6308948

    def generate(self, n):
        result = []
        s, count = 290797, 0
        visited = {s: count}
        while count < n:
            s, count = (s**2) % 50515093, count + 1
            if s in visited:
                break
            result.append(s)
            visited[s] = count
        return result

class SegmentManager():
    def __init__(self, length):
        self.segment_list_map = {}
        for i in range(length):
            self.segment_list_map[i] = (0, length - 1)

    def find(self, pos):
        return self.segment_list_map[pos]

    def split(self, segment, pos):
        begin, end = segment
        for i in range(begin, pos):
            self.segment_list_map[i] = (begin, pos - 1)
        for i in range(pos + 1, end + 1):
            self.segment_list_map[i] = (pos + 1, end)

class Problem():
    def solve(self):
        for n in [10, 10000, 2000000000]:
            print(n, "=>", self.get(n))

    def get(self, n):
        generator = PseudoRandomNumberGenerator()
        period = generator.get_period()
        number_list = generator.generate(n)
        return self.__get_periodic_list(number_list, period, n)

    def __get_periodic_list(self, number_list, period, n):
        min_pos = self.__get_min_element_pos(number_list)
        repeated_count = (n - min_pos - 1) // period

        head_length = min_pos
        tail_length = n - (min_pos + repeated_count * period + 1)
        min_element_interval_count = n * (n + 1) // 2 \
                - head_length * (head_length + 1) // 2 \
                - repeated_count * (period - 1) * period // 2 \
                - tail_length * (tail_length + 1) // 2

        head_sum = self.__get_nonperiodic_list(number_list[0:min_pos])

        repeated_sum = self.__get_nonperiodic_list(number_list[min_pos+1:period] + number_list[0:min_pos]) if repeated_count > 0 else 0
        
        tail_n = n % period
        tail_list = number_list[min_pos + 1:tail_n] if tail_n > min_pos else number_list[min_pos + 1:] + number_list[:tail_n]
        tail_sum = self.__get_nonperiodic_list(tail_list)

        total_sum = min_element_interval_count * number_list[min_pos] \
                + head_sum \
                + repeated_sum * repeated_count \
                + tail_sum
        return total_sum

    def __get_nonperiodic_list(self, number_list):
        number_count = len(number_list)
        sorted_list = sorted([(number_list[i], i) for i in range(number_count)])
        result = 0
        manager = SegmentManager(number_count)
        for i in range(number_count):
            number, pos = sorted_list[i]
            segment = manager.find(pos)
            manager.split(segment, pos)
            begin, end = segment
            result += number * (pos - begin + 1) * (end - pos + 1)
        return result

    def __get_min_element_pos(self, number_list):
        pos = 0
        min_so_far = number_list[0]
        for i in range(1, len(number_list)):
            if number_list[i] < min_so_far:
                pos = i
                min_so_far = number_list[i]
        return pos

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
