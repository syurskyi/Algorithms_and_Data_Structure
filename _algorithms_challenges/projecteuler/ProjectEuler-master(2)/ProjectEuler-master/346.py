import sys

PROBLEM_BOUND = 10**12
BASE_BOUND = 10**6

def get_number(rep, base):
    number = 0
    for digit in rep:
        number *= base
        number += int(digit)
    return number

def generate_repunits(base):
    repunits = []
    for n in range(3, 40):
        number = get_number('1' * n, base)
        if number > PROBLEM_BOUND:
            break
        repunits.append(number)
    return repunits
    
def main():
    all_repunits = [1]
    for base in range(2, BASE_BOUND):
        all_repunits += generate_repunits(base)
    print(sum(set(all_repunits)))
    
if __name__ == '__main__':
    sys.exit(main())
