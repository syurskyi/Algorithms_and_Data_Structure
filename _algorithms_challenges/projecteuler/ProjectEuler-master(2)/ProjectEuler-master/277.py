from sys import exit

class ModifiedCollatzSequenceBuilder():
    def get(self, x):
        steps = []
        while x != 1:
            mod3 = x % 3
            if mod3 == 0:
                x = x // 3
                steps.append('D')
            elif mod3 == 1:
                x = (4 * x + 2) // 3
                steps.append('U')
            elif mod3 == 2:
                x = (2 * x - 1) // 3
                steps.append('d')
        return ''.join(steps)
    
    def backtrace(self, sequence, lower_bound):
        solution, curr = None, None
        init_step = sequence[0]
        if init_step == 'D':
            solution, curr = (3, 0), (1, 0)
        elif init_step == 'U':
            solution, curr = (3, 1), (4, 2)
        elif init_step == 'd':
            solution, curr = (3, 2), (2, 1)
        
        for step in sequence[1:]:
            p, q = curr
            a, b = solution
            if step == 'D':
                if p % 3 == 0 and q % 3 == 0:
                    curr = (p // 3, q // 3)
                else:
                    for r in range(3):
                        if (p*r + q) % 3 == 0:
                            curr = (p, (p*r + q) // 3)
                            solution = (3*a, a*r + b)
            elif step == 'U':
                if p % 3 == 0 and (q - 1) % 3 == 0:
                    curr = (p // 3, (q - 1) // 3)
                else:
                    for r in range(3):
                        if (p*r + q - 1) % 3 == 0:
                            curr = (4*p, (4*(p*r + q) + 2) // 3)
                            solution = (3*a, a*r + b)
            elif step == 'd':
                if p % 3 == 0 and (q - 2) % 3 == 0:
                    curr = (p // 3, (q - 2) // 3)
                else:
                    for r in range(3):
                        if (p*r + q - 2) % 3 == 0:
                            curr = (2*p, (2*(p*r + q) - 1) // 3)
                            solution = (3*a, a*r + b)
        p, q = solution
        return p * ((lower_bound - q) // p + 1) + q
        
def main():
    builder = ModifiedCollatzSequenceBuilder()
    sequence = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'
    x = builder.backtrace(sequence, 10**15)
    assert(x > 10**15)
    assert(builder.get(x).startswith(sequence))
    print(x)
    
if __name__ == '__main__':
    exit(main())
