import itertools
import string
import sys

class Problem():
    def solve(self):
        self.get_maximix_arrangements(11, 2011)
    
    def get_maximix_arrangements(self, train_count, nth):
        max_count_so_far = 1
        max_arrangements_so_far = []
        performance_counter = 0
        for train in itertools.permutations(range(train_count)):
            if train[0] == 0:
                continue
            performance_counter += 1
            if performance_counter % 10000 == 0:
                print(performance_counter, train)
                
            count = self.get_rotation_count(train, train_count)
            if count == max_count_so_far:
                max_arrangements_so_far.append(train)
            elif count > max_count_so_far:
                max_count_so_far = count
                max_arrangements_so_far = [train]
        self.print_max_arrangement(max_arrangements_so_far, nth)
        
    def get_rotation_count(self, train, train_count):
        count = 0
        for carriage in range(train_count):
            if train[carriage] != carriage:
                pos = train.index(carriage)
                if pos != train_count - 1:
                    train = train[:pos] + train[pos:][::-1]
                    count += 1
                train = train[:carriage] + train[carriage:][::-1]
                count += 1
        return count
    
    def print_max_arrangement(self, max_arrangements, nth):
        n = len(max_arrangements)
        if nth > len(max_arrangements) or nth < 1:
            return
        rep = [string.ascii_uppercase[carriage] for carriage in max_arrangements[nth-1]]
        print(''.join(rep))
    
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
