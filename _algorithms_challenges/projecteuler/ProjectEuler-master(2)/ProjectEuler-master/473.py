import sys

class PhigitalRep():
    def get(self, phigital_rep):
        positive_rep = self._get_positive_rep(phigital_rep)
        positive_value = self._get_positive_value(positive_rep)
        negative_rep = self._get_negative_rep(phigital_rep)
        negative_value = self._get_negative_value(negative_rep)
        return [
            positive_value[0] + negative_value[0], 
            positive_value[1] - negative_value[0] + negative_value[1]
        ]
        
    def get_smart(self, palindromic_rep):
        positive_value = self._get_positive_value(palindromic_rep + '0')
        negative_value = self._get_negative_value(palindromic_rep + '00')
        return [
            positive_value[0] + negative_value[0], 
            positive_value[1] - negative_value[0] + negative_value[1]
        ]
        
    def _get_positive_rep(self, phigital_rep):
        phigital_point_pos = phigital_rep.find('.');
        if phigital_point_pos == -1:
            return phigital_rep
        else:
            return phigital_rep[:phigital_point_pos]     
    
    def _get_positive_value(self, positive_rep):
        return self._get_positive_value_impl([int(_) for _ in positive_rep])
        
    def _get_positive_value_impl(self, poly_rep):    
        if len(poly_rep) < 3:
            return poly_rep
        poly_rep[1] += poly_rep[0]
        poly_rep[2] += poly_rep[0]
        return self._get_positive_value_impl(poly_rep[1:])
        
    def _get_negative_rep(self, phigital_rep):
        phigital_point_pos = phigital_rep.find('.');
        if phigital_point_pos == -1:
            return '0'
        else:
            return phigital_rep[phigital_point_pos + 1:][::-1] + '0'
    
    def _get_negative_value(self, negative_rep):
        return self._get_negative_value_impl([int(_) for _ in negative_rep])
        
    def _get_negative_value_impl(self, poly_rep):    
        if len(poly_rep) < 3:
            return poly_rep
        poly_rep[1] -= poly_rep[0]
        poly_rep[2] += poly_rep[0]
        return self._get_negative_value_impl(poly_rep[1:])        
        
class Problem():
    def __init__(self):
        self.phigital_rep = PhigitalRep()
        self.bound = None
        
    """
    Note: We can use '1' to represent palindromic '10.01', or use '10010' to 
          represent '100100.001001'.
    """
    def solve(self):
        for n in [1000, 10**4, 10**5, 10**10]:
            if n <= 10**5:
                print(self.get(n))
            print(self.get_boost(n))
    
    def get_boost(self, bound):
        total_sum_map = {
            2: ['10'],
            6: ['100100'],
        }

        for i in range(8, 100, 2):
            init_rep = '100100' + '0' * (i-6)
            x, y = self.phigital_rep.get_smart(init_rep[:-1])
            assert(x == 0)
            if y > bound:
                break
            
            total_sum_map[i] = [init_rep]
            free_length = i - 6
            for j in total_sum_map:
                if j > free_length:
                    continue
                for free_rep in total_sum_map[j]:
                    next_rep = init_rep[:-j] + free_rep
                    total_sum_map[i].append(next_rep)
        
        total_sum = 1
        for i in total_sum_map:
            for rep in total_sum_map[i]:
                x, y = self.phigital_rep.get_smart(rep[:-1])
                assert(x == 0)
                if y <= bound:
                    #print(y, rep)
                    total_sum += y
        return total_sum
            
    def get(self, bound):
        self.bound = bound
        # Special case: '1', '10.01'
        total_sum = 3
        bfs_queue = ['10010'] 
        while bfs_queue:
            top = bfs_queue[0]
            bfs_queue.pop(0)
            is_unbounded, is_integer, integer_value = self._validate(top)
            if is_unbounded:
                continue
            if is_integer:
                total_sum += integer_value
                #print(top + '0', integer_value)
            # Push next smart_rep
            bfs_queue.append(top + '0') 
            if top[-1] == '0' and top[-2] == '0':
                bfs_queue.append(top + '1')
        return total_sum
        
    def _validate(self, smart_rep):
        x, y = self.phigital_rep.get_smart(smart_rep)
        if x == 0 and y > self.bound:
            return True, None, None
        if 5 * x**2 > (2 * self.bound - x - 2 * y)**2:
            return True, None, None
        if x == 0:
            return False, True, y
        else:
            return False, False, None
            
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
