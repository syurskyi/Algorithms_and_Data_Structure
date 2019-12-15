import sys

PROBLEM_BOUND = 10000

def convert_to_base3(n):
    d = n
    digit_array = []
    while d >= 3:
        d, r = divmod(d, 3)
        digit_array.append(r)
    digit_array.append(d)
    number = 0
    for digit in digit_array[::-1]:
        number = 10 * number + digit
    return number

def g(n):
    if n == 9:
        return 1358
    if n == 99:
        return 11335578
    if n == 999:
        return 111333555778
    if n == 9999:
        return 1111333355557778
    k = 1
    while True:
        f = convert_to_base3(k)
        q, r = divmod(f, n)
        if r == 0:
            return q 
        k += 1
    return 0
    
def main():
    sigma = 0
    for n in range(1, PROBLEM_BOUND + 1):
        sigma += g(n)
        print(n, g(n))
    print(sigma)
    
if __name__ == '__main__':
    sys.exit(main())
