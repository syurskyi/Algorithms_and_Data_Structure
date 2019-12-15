import sys

def get_number(factors):
    number = 1
    for factor in factors:
        number *= factor
    return number

def get_sigma(factors):
    factor_counting = {}
    for factor in factors:
        if factor in factor_counting:
            factor_counting[factor] += 1
        else:
            factor_counting[factor] = 1
    sigma = 1
    for factor in factor_counting:
        sigma *= (2 * factor_counting[factor] + 1)
    return sigma
    
def main():
    factors = [2, 2, 2, 3, 3, 3, 5, 5, 7, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    number = get_number(factors)
    solution_count = (int)(get_sigma(factors)/2) + 1
    print(number)
    print(solution_count)
    if solution_count > 4000000:
        print('''Found''')
    else:
        print('''Not found''')
        
if __name__ == '__main__':
    sys.exit(main())
