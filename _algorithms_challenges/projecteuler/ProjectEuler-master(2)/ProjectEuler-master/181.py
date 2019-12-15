import sys

class Counting():
    def __init__(self, black, white):
        self.count_cache = {}
        self.total_count = self.__count(black, white)

    def get(self):
        return self.total_count

    def __count(self, black, white):
        return self.__count_with_prefix((0, 0), black, white)

    def __count_with_prefix(self, root_prefix, black, white):
        if root_prefix not in self.count_cache:
            self.count_cache[root_prefix] = {}
        object_pair = (black, white)
        if object_pair not in self.count_cache[root_prefix]:
            root_black, root_white = root_prefix
            if black == 0 and white == 0:
                self.count_cache[root_prefix][object_pair] = 1
            elif root_white > white or (root_white == white and root_black > black):
                self.count_cache[root_prefix][object_pair] = 0
            else:
                count = 0
                prefix_list = self.__get_prefix_list(root_prefix, black, white)
                for prefix in prefix_list:
                    prefix_black, prefix_white = prefix
                    rest_black = black - prefix_black
                    rest_white = white - prefix_white
                    count += self.__count_with_prefix(prefix, rest_black, rest_white)
                self.count_cache[root_prefix][object_pair] = count
        return self.count_cache[root_prefix][object_pair]
        
    def __get_prefix_list(self, root_prefix, black, white):
        root_black, root_white = root_prefix
        prefix_list = []
        for i in range(root_black, black + 1):
            prefix_list.append((i, root_white))        
        for j in range(root_white + 1, white + 1):
            for i in range(black + 1):
                prefix_list.append((i, j))

        top_black, top_white = prefix_list[0]
        if top_black == 0 and top_white == 0:
            prefix_list.pop(0)
        return prefix_list

class Problem():
    def solve(self):
        for black, white in [(3, 1), (40, 60)]:
            print(black, white, "=>", self.get(black, white))

    def get(self, black, white):
        return Counting(black, white).get()

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
