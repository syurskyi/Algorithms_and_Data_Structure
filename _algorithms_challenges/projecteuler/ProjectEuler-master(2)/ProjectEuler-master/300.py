from ast import literal_eval
import itertools
import sys

class Folding():
    def build(self, dim):
        vaild_contacts = set()
        initial_state = ([(0, 0), (0, 1)], False)
        dfs_stack = [initial_state]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while dfs_stack:
            top_folding, top_turn = dfs_stack[-1]
            dfs_stack.pop()
            if self.__is_overlapping(top_folding):
                continue
            if len(top_folding) == dim:
                contact = self.__get_contact(top_folding)
                vaild_contacts.add(str(contact))
                continue
            last_x, last_y = top_folding[-1]
            for direction_x, direction_y in directions:
                next_turn = top_turn
                if top_turn is False:
                    if direction_x == -1 and direction_y == 0:
                        continue
                    elif direction_x == 1 and direction_y == 0:
                        next_turn = True
                next_spot = (last_x + direction_x, last_y + direction_y)
                next_state = (top_folding + [next_spot], next_turn)
                dfs_stack.append(next_state)
        return [literal_eval(_) for _ in vaild_contacts]

    def __is_overlapping(self, folding):
        visited_spots = set([str(_) for _ in folding])
        return len(folding) != len(visited_spots)

    def __get_contact(self, folding):
        rv = []
        n = len(folding)
        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(folding[i][0] - folding[j][0]) + abs(folding[i][1] - folding[j][1])
                if distance == 1:
                    rv.append(2**i + 2**j)
        return sorted(rv)

class Problem():
    def solve(self):
        self.get(15)
    
    def get(self, dim):
        folding = Folding()
        contacts = folding.build(dim)
        print("contact search space size =>", len(contacts))
        
        count_map = {}
        protein_count = 0
        for protein, reversed_protein in self.__protein_iterator(dim):
            if protein in count_map:
                continue
            count = 0
            for contact in contacts:
                curr_count = 0
                for point in contact:
                    if protein & point == point:
                        curr_count += 1
                count = max(count, curr_count)
            count_map[protein] = count
            count_map[reversed_protein] = count
            protein_count += 1
            print(protein_count, protein, "=>", count)
        total_count = 0
        for protein in count_map:
            total_count += count_map[protein]
        print(total_count)
        print(self.__format_number(total_count * 5**dim, dim))

    def __protein_iterator(self, n):
        for protein in range(2**n):
            reversed_protein = sum(1<<(n-1-i) for i in range(n) if protein>>i & 1)
            yield protein, reversed_protein

    def __format_number(self, number, pos):
        rep = str(number)
        if len(rep) > pos:
            rep = rep[:len(rep) - pos] + "." + rep[len(rep) - pos:]
        else:
            rep = "0." + "".join(["0" for i in range(pos - len(rep))]) + rep
        while rep[-1] == "0":
            rep = rep[:-1]
        return rep

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
